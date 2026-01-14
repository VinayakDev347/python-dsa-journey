# Count vowels in a string
words = input("Enter some words...lets check how many vowels are there...")
count = 0

for i in words:
    if i in "aeiouAEIOU":
        count += 1
print(count)

# Reverse a string
words = "hello"
re = ""
for i in words:
    re = i + re

print(re)

# Check palindrome string
words = "sos"
re = ""
for i in words:
    re = i + re
if re == words:
    print("Its palindrome")
else:
    print("Not Palindrom")

# Count frequency of each character
words = "sossee"
frq = {}
for ch in words:
    if ch in frq:
        frq[ch] += 1
    else:
        frq[ch] = 1
print(frq)