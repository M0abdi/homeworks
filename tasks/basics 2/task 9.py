def factorial(n, memo={}):
    if n in memo: return memo[n]
    if n <= 1: return 1
    memo[n] = n * factorial(n-1, memo)
    return memo[n]

def sum_factorials(n):
    return sum(factorial(i) for i in range(1, n+1))

print(sum_factorials(5)) # 1!+2!+3!+4!+5!
