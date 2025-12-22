def f_strings(lst):
    return [s for s in set(lst) if len(s) > 5]

print(f_strings(["apple", "banana", "cherry", "apple", "mangoes"]))
