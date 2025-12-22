class ZipSequences:
    def __init__(self, *sequences):
        self.sequences = sequences
        self.current_index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_index >= min(len(seq) for seq in self.sequences):
            raise StopIteration
        
        result = tuple(seq[self.current_index] for seq in self.sequences)
        self.current_index += 1
        return result

def zip_sequences(*sequences):
    return ZipSequences(*sequences)


print("=== Task 2: Zip Sequences ===")
print("zip_sequences([1, 2], [3, 4], [5, 6]):")
for item in zip_sequences([1, 2], [3, 4], [5, 6]):
    print(item, end=" ")
print("\n")
