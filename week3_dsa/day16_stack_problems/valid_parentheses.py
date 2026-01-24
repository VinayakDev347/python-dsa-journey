# Input: "()[]{}" → True
# Input: "([)]" → False

def check_para(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in pairs:  # closing bracket
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:  # opening bracket
            stack.append(ch)

    return len(stack) == 0
            



s = "()[]{}"
print(check_para(s))