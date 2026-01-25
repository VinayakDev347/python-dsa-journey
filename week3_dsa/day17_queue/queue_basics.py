from collections import deque

queue = deque()

queue.append(10)     # enqueue
queue.append(20)
queue.append(30)

print(queue.popleft())  # dequeue → 10
print(queue)
