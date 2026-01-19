# sum of digit
def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

print(sum_digits(1234))

# Count digit
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

print(count_digits(4567))

# count palindrom number 
def is_palindrome_num(n, rev=0):
    if n == 0:
        return rev
    return is_palindrome_num(n // 10, rev * 10 + n % 10)

num = 121
print(num == is_palindrome_num(num))

