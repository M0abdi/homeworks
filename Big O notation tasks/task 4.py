def move_zeros(nums):
    non_zero_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
            non_zero_pos += 1
    return nums

# Example
print(move_zeros([0, 1, 0, 3, 12]))  
print(move_zeros([0, 0, 1]))    
