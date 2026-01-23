# Check balanced parentheses
def is_balanced(expression):
    stack = []

    for ch in expression:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0


# Test cases
print(is_balanced("((a+b))"))   # True
print(is_balanced("(a+b))"))    # False
