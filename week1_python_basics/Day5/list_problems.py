
"""
# Find maximum element in a list

numbers = [12, 45, 7, 89, 34]
max_num = 0
for i in numbers:
    if i > max_num:
        max_num = i

print("maximum number is : ",max_num)


# Find minimum element in a list
numbers = [12, 45, 7, 89, 34]
min_num = numbers[0]

for i in numbers:
    if i < min_num:
        min_num = i

print("Minimum number is : ",min_num)

# Sum of elements in a list
numbers = [1,2,3,4,5]
sum = 0 
for i in numbers:
    sum += i 
print("Total sum is : ",sum)


# Count even and odd numbers
numbers = [1, 2, 3, 4, 5, 6]
odd = 0
even = 0
for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("No of Odd: ",odd)
print("No of Even: ",even)

# Search element in a list (Linear Search)
numbers = [5, 10, 15, 20, 25]
key = 15
found = False

for i in numbers:
    if i == key:
        found = True
        break
if found:
    print("Element Founded")
else:
    print("Element not Found")

# Reverse a list (without using reverse())
numbers = [1, 2, 3, 4, 5]
rev = []
for i in range(len(numbers)-1,-1,-1):
    rev.append(numbers[i])

print(rev)
"""

# Remove duplicates from list
numbers = [1, 2, 2, 3, 4, 4, 5]
uni = []

for num in numbers:
    if num not in uni:
        uni.append(num)
print(uni)