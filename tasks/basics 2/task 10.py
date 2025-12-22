def check_2d_array(arr):
    vowels = "aeiouAEIOU"
    for col in range(len(arr[0])):
        count = sum(1 for row in arr if row[col][0] in vowels)
        if count > 2:
            return False
    return True

data = [["apple", "dog", "owl"],
        ["orange", "cat", "egg"],
        ["ice", "rat", "ant"]]

print(check_2d_array(data))
