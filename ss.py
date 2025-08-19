def find_missing_number(arr):
    n = len(arr) + 1  # Since one number is missing
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example
nums = [1, 2, 4, 5, 6]  # Missing 3
print(find_missing_number(nums))  # Output: 3