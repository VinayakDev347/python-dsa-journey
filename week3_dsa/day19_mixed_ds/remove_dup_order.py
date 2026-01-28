def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


# Test
nums = [1, 2, 2, 3, 1, 4]
print("After removing duplicates:", remove_duplicates(nums))
