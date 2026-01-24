class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
            return self.stack

    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

# create object of MinStack
ms = MinStack()

ms.push(5)
ms.push(3)
ms.push(7)

print("Top element:", ms.top())      # 7
print("Minimum:", ms.getMin())       # 3

ms.pop()

print("Top after pop:", ms.top())    # 3
print("Minimum after pop:", ms.getMin())  # 3
