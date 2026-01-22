# Factorial (function)
def find_factorial(num):
    if num == 1:
        return 1
    return num * find_factorial(num-1)

print(find_factorial(5))

# First non-repeating character
def check_nonrepeating_chr(txt):
    frq = {}
    for i in txt:
        frq[i] = frq.get(i,0)+1

    for i in txt:
        if frq[i] == 1:
            return i

print(check_nonrepeating_chr("happyay"))

# Anagram check
def check_anagram(txt1,txt2):
    if len(txt1) != len(txt2):
        return False
    
    frq = {}
    for i in txt1:
        frq[i] = frq.get(i,0)+1

    for i in txt2:
        if i not in frq:
            return False
        frq[i] -= 1
    return True

print(check_anagram("silent","listen"))
