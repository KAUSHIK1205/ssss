def max_difference_ordered(arr):
    if len(arr) < 2:
        return 0
    min_val = arr[0]
    max_diff = arr[1] - arr[0]
    for i in range(1, len(arr)):
        max_diff = max(max_diff, arr[i] - min_val)
        min_val = min(min_val, arr[i])
    return max_diff

# Example
nums = [7, 1, 5, 3, 6, 4]
print(max_difference_ordered(nums))  # Output: 5