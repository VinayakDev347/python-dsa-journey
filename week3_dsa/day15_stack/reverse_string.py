# Reverse a string using stack
def reverse_string_using_stack(s):
    stack = []

    # Push characters into stack
    for ch in s:
        stack.append(ch)

    reversed_str = ""

    # Pop characters from stack
    while stack:
        reversed_str += stack.pop()

    return reversed_str

print(reverse_string_using_stack("hello"))

