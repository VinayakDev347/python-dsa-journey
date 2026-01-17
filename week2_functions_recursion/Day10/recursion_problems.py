# Factorial using recursion

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Print numbers from 1 to n
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n)

print_1_to_n(5)

# Reverse a string (recursively)
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]

print(reverse_string("python"))