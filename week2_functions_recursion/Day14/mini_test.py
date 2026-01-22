# Reverse string (recursion)
def reverse_str(txt):
    if txt == "":
        return ""
    return reverse_str(txt[1:]) +   txt[0] 

print(reverse_str("hello"))

# Second largest number
def check_sec_larg(num):
    first = second =- 1
    for i in num:
        if i > first:
            second = first
            first = i
        elif i > second and i != first:
            second = i
    return second         

num = [1,2,3,4,5]
print(check_sec_larg(num))

# Digital root
def digital_root(n):
    if n < 10:
        return n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return digital_root(s)

print(digital_root(9875))

# First repeating character
def first_repeating_char(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return None

print(first_repeating_char("abca"))