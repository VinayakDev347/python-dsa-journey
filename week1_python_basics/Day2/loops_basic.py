# Day 2

# for loop
for i in range(1,6):
    print(i,end=",")            #1,2,3,4,5,
print()

for i in range(6):
    print(i,end=",")            #0,1,2,3,4,5,
print()

abc = ["apple","rose","hello"]
for i in abc:
    print(i,end=" ")            #apple rose hello 

for i in range(1,10,2):
    print(i)                    #3,5,7,9

for i in range(2,10,2):
    print(i)                    #2,4,6,8

for i in range(5,1,-1):
    print(i)                    #5,4,3,2


# while loop
i = 0
while i<=5:
    print(i,end=" ")           #0 1 2 3 4 5
    i+=1
