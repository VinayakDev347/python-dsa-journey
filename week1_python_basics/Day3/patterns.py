# Right Angle Star Pattern
num = 5


for i in range(num+1):
    for j in range(i):
        print("*",end=" ")
    print()

# Number Triangle
for i in range(num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# Repeated Number Pattern
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

# Inverted Star Pattern
for i in range(num,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# Square Pattern
for i in range(num+1):
    for j in range(num):
        print("*",end=" ")
    print()

# Alphabet Pattern
n = 4
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()
