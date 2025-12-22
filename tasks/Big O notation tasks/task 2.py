

def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return -1



# Example
arr = [1, 3, 5, 7, 9]
print(two_sum_sorted(arr, 12))  
print(two_sum_sorted(arr, 20))
