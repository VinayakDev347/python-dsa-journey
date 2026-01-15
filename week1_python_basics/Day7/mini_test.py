# Q1: Count digits
"""
num = 1232
count = 0 
while num > 0:
    count += 1
    num //= 10
print(count)
"""

# Q2: Find duplicates in list
"""
num = [1,2,3,1,2]
check = {}
duplicate = []
for i in num:
    if i in check:
        duplicate.append(i)
    else:
        check[i] = 1
print(duplicate)
"""

# Q3: First non-repeating character
"""
text = "hello"
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

for ch in text:
    if freq[ch] == 1:
        print(ch)
        break
"""

# Q4: Check anagram
"""
s1 = "listen"
s2 = "silent"

news1 = sorted(s1)
news2 = sorted(s2)
if news1 == news2:
    print("Its Anagram")
else:
    print("Not Anagram")

# ------------- another method -------------------

for ch in s1:
    freq1[ch] = freq1.get(ch, 0) + 1

for ch in s2:
    freq2[ch] = freq2.get(ch, 0) + 1

print(freq1 == freq2)
"""
