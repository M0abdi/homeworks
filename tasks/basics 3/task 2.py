
p_numbers = int(input(" give me a number: "))


def p_numbers(n):
    if n == 0:
        return
    print(n)
    p_numbers( n - 1 )

print(p_numbers)
