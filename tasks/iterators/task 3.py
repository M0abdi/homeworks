def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # in here we Checking odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    """Generator that yields all prime numbers less than n."""
    if n > 1:
        yield 1  
    for num in range(2, n):
        if is_prime(num):
            yield num


print("=== Task 3: Prime Number Generator ===")
print("generate_primes(8):")
for prime in generate_primes(8):
    print(prime, end=" ")
print("\n")
