#Input: [4, 5, 2, 25]
# Output: [5, 25, 25, -1]

def next_great(arr):
    stack =[]
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)

    return result


arr = [4, 5, 2, 25]
print(next_great(arr))