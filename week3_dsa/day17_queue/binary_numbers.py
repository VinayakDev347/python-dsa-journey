from collections import deque

def generate_binary(n):
    q = deque()
    q.append("1")

    for _ in range(n):
        curr = q.popleft()
        print(curr)

        q.append(curr + "0")
        q.append(curr + "1")

generate_binary(5)
