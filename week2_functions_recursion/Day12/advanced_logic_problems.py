# most frequent charactor
def most_frequent_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    max_char = s[0]
    for ch in freq:
        if freq[ch] > freq[max_char]:
            max_char = ch

    return max_char

print(most_frequent_char("programming"))

# Second largest number in list
def second_largest(nums):
    first = second = -1

    for n in nums:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n

    return second

print(second_largest([10, 5, 20, 8]))

#remove duplicate
def remove_duplicates(nums):
    seen = {}
    result = []

    for n in nums:
        if n not in seen:
            seen[n] = True
            result.append(n)

    return result

print(remove_duplicates([1, 2, 2, 3, 1, 4]))
