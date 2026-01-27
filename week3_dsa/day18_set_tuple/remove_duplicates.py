# nums = [1, 2, 2, 3, 4, 4]
# Output:- [1, 2, 3, 4]

# TASK 1: Remove duplicates using set

nums = [1, 2, 2, 3, 4, 4]

# convert list to set, then back to list
unique_nums = list(set(nums))

print("Original list:", nums)
print("After removing duplicates:", unique_nums)
