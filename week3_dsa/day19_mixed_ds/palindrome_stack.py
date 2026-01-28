def is_palindrome(s):
    stack = []

    # push all characters to stack
    for ch in s:
        stack.append(ch)

    # compare while popping
    for ch in s:
        if ch != stack.pop():
            return False

    return True


# Tests
print("madam →", is_palindrome("madam"))
print("hello →", is_palindrome("hello"))
