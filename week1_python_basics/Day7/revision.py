# 1. Sum of digits - 233
"""
num = int(input("Enter some digits to find its sum: "))
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
print("Sum of the given number is :",sum)


# 2. Reverse number
num = int(input("Enter number: "))
rev = 0
while num > 0:
    rev = rev * 10 + (num % 10)
    num //= 10
print("Reverse:", rev)

# 3. List max
numbers = [4, 2, 9, 1]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(max) 
"""
# 4. String palindrome
words = "soss"
rev = ""
for i in words:
    rev = i + rev
if rev == words:
    print("Its Palindrom")
else:
    print("Not Palindrom")