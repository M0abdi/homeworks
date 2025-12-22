

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    fib_seq = fibonacci(n - 1)
    fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq



print(fibonacci(7))  
