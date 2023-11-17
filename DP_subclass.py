class Sequence:
    def __init__(self, id, seq):
        self._id = id
        self._seq = seq
    #Making the getter for both classes

    @property
    def id(self):
        return self._id
    
    @property
    def seq(self):
        return self._seq
    
    def fasta_file(self):
        return f'>{self.id}\n{self.seq}\n'
    
class DNASequence(Sequence):
    #defining GC content in this superclass
    def get_gc_content(self, dp=3):
        c_count = self.seq.count('C')
        g_count = self.seq.count('G')
        gc_content = (c_count + g_count) / len(self.seq)
        return round(gc_content, dp)
    #defining translate function in this superclass
    def translate(self):
        bases = 'tcag'.upper()
        codons = [a + b + c for a in bases for b in bases for c in bases]
        amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
        codon_table = dict(zip(codons, amino_acids))
        protein_seq = ''
        for s in range(0, len(self.seq)-2, 3):
            codon = self.seq[s:s+3]
            aa = codon_table[codon]
            protein_seq +=aa
        return protein_seq
    
    #Defining the method to get protein length to both dna & protein sequences
    def seq_length(self):
        return len(self.seq) //3
    
class ProteinSequence(Sequence):
    #adding the description property to the protein sequence class which isnt in the superclass
    def __init__(self, id, seq, descr='NA'):
        super().__init__(id, seq)
        self._descr = descr

    @property
    def descr(self):
        return self._descr
    
    #Method to calculate percentage that are hydrophobic
    def calc_hydrophobic(self, dp=2):
        A_count = self.seq.count('A')
        I_count = self.seq.count('I')
        L_count = self.seq.count('L')
        M_count = self.seq.count('M')
        F_count = self.seq.count('F')
        W_count = self.seq.count('W')
        Y_count = self.seq.count('Y')
        V_count = self.seq.count('V')
        hydrophobic_residue = (A_count + I_count + L_count+ M_count + F_count+ W_count + Y_count) / len(self.seq)
        return round(hydrophobic_residue, dp)
    
    def seq_length(self):
        return len(self.seq)
    