# "abcde" → True
# "hello" → False

# TASK 3: Check if string has all unique characters

def has_unique_characters(s):
    return len(s) == len(set(s))


# Test cases
s1 = "abcde"
s2 = "hello"

print(f"{s1} →", has_unique_characters(s1))
print(f"{s2} →", has_unique_characters(s2))
