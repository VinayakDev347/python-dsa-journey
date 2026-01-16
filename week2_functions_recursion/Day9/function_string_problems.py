# First non-repeating character
def find_nonrep(text):
    dupli = {}
    for i in text:
        dupli[i] = dupli.get(i,0) + 1

    for i in text:
        if dupli[i] == 1:
            return i
        
    return None

print(find_nonrep("aabbcde"))

# Check anagram
def check_anagrm(txt1,txt2):
    t1 = txt1.lower()
    t2 = txt2.lower()

    if len(t1) != len(t2):
        return False
    
    freq = {}
    for i in t1:
        freq[i] = freq.get(i,0)+1
        
    for i in t2:
        if i not in freq:
            return False
        freq[i] -= 1

    return True

print(check_anagrm("sos","oss"))