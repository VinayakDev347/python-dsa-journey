# Day 8: Function Basics

def greet():
    print("Hello, Welcome!")

greet()

def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

def is_even(num):
    return num % 2 == 0

print(is_even(10))
print(is_even(7))
