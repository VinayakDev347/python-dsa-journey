# String length
def string_length(s):
    if s == "":
        return 0
    return 1 + string_length(s[1:])

print(string_length("python"))


# Check palindrom
def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

print(is_palindrome("madam"))
print(is_palindrome("python"))
