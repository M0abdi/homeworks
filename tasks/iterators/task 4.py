def generate_combinations(sequence, k):
    """Generate all combinations of length k from sequence."""
    n = len(sequence)
    
    # Base case: if k is 0 or k > n, no combinations
    if k == 0:
        yield ()
        return
    if k > n:
        return
    
    # Recursive generator
    def helper(start, current):
        if len(current) == k:
            yield tuple(current)
            return
        
        for i in range(start, n):
            current.append(sequence[i])
            yield from helper(i + 1, current)
            current.pop()
    
    yield from helper(0, [])


print("$$$ Combinations $$$")
print("\n")
print("generate_combinations([1, 2, 3], 2):")
for combo in generate_combinations([1, 2, 3], 2):
    print("\n")
    print(combo, end=" ")
print("\n")
