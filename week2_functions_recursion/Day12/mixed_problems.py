# First repeating character
def first_repeating_char(s):
    seen = set()

    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)

    return None

print(first_repeating_char("abca"))

# sum of digits until single digit (recursion)
def digital_root(n):
    if n < 10:
        return n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return digital_root(s)

print(digital_root(9875))
