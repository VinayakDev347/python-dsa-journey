# List
numbers = [10, 20, 30, 40, 50]

print(numbers)
print(type(numbers))

# Access the element
print(numbers[0])
print(numbers[-1])

# Loop through list
for i in numbers:
    print(i)

# Add element
numbers.append(60)
print(numbers)

# Remove element
numbers.remove(20)
print(numbers)

# Length of list
print(len(numbers))