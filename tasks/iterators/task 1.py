class ChainSequences:
    def __init__(self, *sequences):
        self.sequences = sequences
        self.current_seq = 0
        self.current_index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current_seq < len(self.sequences):
            if self.current_index < len(self.sequences[self.current_seq]):
                value = self.sequences[self.current_seq][self.current_index]
                self.current_index += 1
                return value
            else:
                self.current_seq += 1
                self.current_index = 0
        
        raise StopIteration

def chain_sequences(*sequences):
    return ChainSequences(*sequences)


print("**** Task 1: Chain Sequences ****")
print("chain_sequences([1, 2, 3], [4], [5]):")
for item in chain_sequences([1, 2, 3], [4], [5]):
    print(item, end=" ")
print("\n")
