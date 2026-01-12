def demo_fun():
    print("You called Function...")

demo_fun()
demo_fun()

def add(num1,num2):
    return num1 + num2

result = add(1,5)
print(result)

def check_even(num):
    if num % 2 == 0:
        print("Its Even")
    elif num % 2 == 1:
        print("Its Odd")
    else:
        print("Invalid number")

check_even(2)
check_even(3)
check_even(9)
