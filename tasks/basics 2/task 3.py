def rvrs_list(lst):
    rev = []
    for i in range(len(lst) - 1, -1, -1):
        rev.append(lst[i])
    return rev

print(rvrs_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]))
