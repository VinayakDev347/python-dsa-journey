"""
# Print numbers from 1 to N
num = int(input("Enter the Number : "))
for i in range(1,num+1):
    print(i)


# Print even numbers from 1 to N
num1 = int(input("Enter the Number : "))
for i in range(2,num1+2,2):
    print(i)
print("\n---Another method---\n")
for i in range(1,num1+1):
    if i % 2 == 0:
        print(i)

# Sum of first N numbers
num = int(input("Enter the number: "))
sum = 0
for i in range(num+1):
    sum += i
print(sum)


# Count digits of a number
num = int(input("Enter the number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print(count)


# Reverse a number
num = int(input("Enter the number: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10 
print(reversed_num)


# Check palindrome number
num = int(input("Enter number: "))
temp = num
reversed_num = 0
while num > 0:
    digit =num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
if reversed_num == temp:
    print("Its Palindrome")
else:
    print("Not Palindrom")

# Multiplication table
num = int(input("Enter the number to see its multiplication table: "))
for i in range(1,num+1):
    print(f"{i} * {num} = {i*num}")
"""

# Factorial of a number
num = int(input("Enter the number: "))
fact = 1 
for i in range(1,num+1):
    fact *= i
print(fact)