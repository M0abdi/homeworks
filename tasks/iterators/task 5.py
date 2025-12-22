def flatten_iterate(nested_list):
    """Flatten a nested list using recursion."""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_iterate(item)
        else:
            yield item


print("=*= Multi-dimensional Array Iterator =*=")
print("\n")
print("flatten_iterate([1, 2, [3, [4], 5]]):")
for item in flatten_iterate([1, 2, [3, [4], 5]]):
    print(item, end=" ")
print("\n")
