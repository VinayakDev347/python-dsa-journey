# Remove adjacent duplicates
def remove_adjacent_duplicates(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()   # remove duplicate
        else:
            stack.append(ch)

    return "".join(stack)


# Example
print(remove_adjacent_duplicates("abbaca"))
