# Input: "23*54*+9-"
# Output: 17


def evaluatePostfix(exp):
    stack = []

    for ch in exp:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(int(a / b))

    return stack[-1]

exp = "23*54*+9-"
print(evaluatePostfix(exp))