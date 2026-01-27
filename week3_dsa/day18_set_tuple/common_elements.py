# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# Output:- {3, 4}

# TASK 2: Find common elements between two lists

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

# convert to sets
set_a = set(a)
set_b = set(b)

# find intersection
common = set_a & set_b

print("List A:", a)
print("List B:", b)
print("Common elements:", common)
