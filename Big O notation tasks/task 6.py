def three_sum_sorted(arr, target):
    n = len(arr)
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == target:
                return (arr[i], arr[left], arr[right])
            elif total < target:
                left += 1
            else:
                right -= 1
    return -1

# Example
arr = [1, 3, 5, 7, 9, 11]
print(three_sum_sorted(arr, 15))  
print(three_sum_sorted(arr, 30))  
