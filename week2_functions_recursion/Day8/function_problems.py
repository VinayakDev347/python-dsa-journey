# Sum of digits
"""
def findsum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

print(findsum(123))
"""

# Reverse a number
"""
def rev_num(num):
    rev = 0
    while num > 0:
        rev = 10 * rev + (num % 10)
        num //= 10
    return rev

print(rev_num(123))

# Check palindrome number

def checkpalindrom(num):
    return num == rev_num(num)

print(checkpalindrom(121))
"""

# Count vowels in string
"""
def count_vow(text):
    count = 0
    for i in text:
        if i in "aeiouAEIOU":
            count += 1
    return count

print(count_vow("aaeebbu"))
"""