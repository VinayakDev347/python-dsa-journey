from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    result = []

    for i in range(len(nums)):
        # remove elements out of window
        if dq and dq[0] == i - k:
            dq.popleft()

        # remove smaller elements from back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # window starts when i >= k-1
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# Test
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print("Sliding window maximum:", max_sliding_window(nums, k))
