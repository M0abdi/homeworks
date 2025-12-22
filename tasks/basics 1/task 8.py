
n = input("Enter number: ")
expanded = []
for i, d in enumerate(n):
    if d != "0":
        expanded.append(d + "0"*(len(n)-i-1))
print(" + ".join(expanded))
