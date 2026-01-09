"""
# Even or Odd---------------------------------------
num = int(input("Enter Number:"))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# Largest of Two Numbers  
num1 = int(input("Enter first Number:"))
num2 = int(input("Enter second Number:"))
if num1 > num2:
    print("Num1 is greater than Num2")
else:
    print("Num2 is greater than Num1")


# Largest of Three Numbers---------------------------------------
num1 = int(input("Enter first Number:"))
num2 = int(input("Enter second Number:"))
num3 = int(input("Enter third Number:"))
if num1>num2 and num1>num3:
    print("Num1 is Greater")
elif num2 > num1 and num2 > num3:
    print("Num2 is Greater")
else:
    print("Num3 is Greater")

# Check Leap Year---------------------------------------
year = int(input("Enter the Year...You want to check leap year!!!"))
if year % 400 == 0:    
    print("Its leapYear!!!")
elif year%4 == 0 and year%100 != 0:
    print("Its leapYear!!!")
else:
    print("No ")

# Positive / Negative / Zero---------------------------------------
num = int(input("Enter a number: "))
if num > 0:
    print("Entered number is Positive")
elif num == 0:
    print("Entered number is Zero")
elif num < 0:
    print("Entered number is Negative")
else:
    print("Invalid number")

"""