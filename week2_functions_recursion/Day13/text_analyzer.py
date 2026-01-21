# find the count of given text
def count_txt(txt):
    return len(txt)

# find the count of words
def count_words(txt):
    return len(txt.split())

# find the count of vowel
def count_vowel(txt):
    count = 0
    for i in txt:
        if i in "aeiouAEIOU":
            count += 1
    return count

# find the most frequent character from the txt
def most_frequent_chr(txt):
    frq = {}
    for i in txt:
        frq[i] = frq.get(i,0) + 1

    max_char = txt[0]
    for i in frq:
        if frq[i] > frq[max_char]:
            max_char = i 
    
    return max_char

# find the first non repeating character from the txt

def first_non_repeating_chr(txt):
    frq = {}
    for i in txt:
        frq[i] = frq.get(i,0) + 1
        
    for i in txt:
        if frq[i] == 1:
            return i

# check given txt is palindrom or not  
def is_palindrome(txt):
    txt = txt.replace(" ", "").lower()
    return txt == txt[::-1]


""" main function calling part """
# txt = input("Enter Your Text: ")
txt = "heyyy im"
txt1 = "sos"
print(count_txt(txt))
print(count_words(txt))
print(count_vowel(txt))
print(count_vowel(txt))
print(first_non_repeating_chr(txt))
print(is_palindrome(txt1))


