class ParseFastaFile:
    
    def __init__(self, file):
        self._file = file

      # getter for file
    @property
    def file(self):
        return self._file
    
    #defining the open fasta file function
    def parse_fasta_file(self):
        with open(self.file) as input:
            for line in input:
                id = line.rstrip().lstrip('>')
                seq = next(input) 
                seq = seq.rstrip()
                sequence_instance = DNASequence(id, seq)
                yield sequence_instance