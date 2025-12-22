

def safeget_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None


my_list = [1, 2, 3, 4, 5]
print(safeget_element(my_list, 2))   
print(safeget_element(my_list, 10))  
