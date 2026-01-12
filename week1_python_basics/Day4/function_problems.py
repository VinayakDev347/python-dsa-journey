"""
# Function to check Even or Odd
def checking(num1):
    if num1 % 2 == 0:
        print("Its Even")
    elif num1 % 2 == 1:
        print("Its Odd")
    else:
        print("Invalid...")

checking(2)
checking(3)
checking(1)


# Function to find maximum of two numbers
def find_max(num1,num2):
    if num1 > num2:
        return num1 
    return num2 

print(find_max(2,19))
print(find_max(100,40))

# Function to find maximum of three numbers
def find_max3(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num3 and num2 > num1:
        print(num2)
    else:
        print(num3)

find_max3(2,3,4)
find_max3(5,6,2)
find_max3(100,2,3)

# Function to calculate factorial
def find_fact(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

print(find_fact(5))

# Function to reverse a number
def rev(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev

print(rev(239))


# Function to check palindrome number
def check_palindrom(num):
        return num == rev(num)          # from upper fun rev is called from here
    
print(check_palindrom(121))


# Function to print multiplication table
def multiplication_tb(num):
    for i in range(1,11):
        print(f'{i} X {num} = {i*num}')

multiplication_tb(2)
"""

