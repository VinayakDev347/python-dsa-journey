def first_repeating_char(s):
    seen = set()

    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)

    return None


# Test
s = "programming"
print("First repeating character:", first_repeating_char(s))
