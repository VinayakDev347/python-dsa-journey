def countdown(n):
    if n == 0:          # base case
        return
    print(n)
    countdown(n - 1)    # recursive call

countdown(5)

# Sum of numbers (1 to n)
def sumofnum(n):
    if n == 1:
        return 1
    return n + sumofnum(n - 1)

print(sumofnum(5))