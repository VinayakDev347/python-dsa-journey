# Check prime number
def check_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
        
print(check_prime(7))
print(check_prime(21))

# Factorial using function
def find_fact(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

print(find_fact(5))


# Find maximum in list
def find_max(nums):
    max = nums[0]
    for i in nums:
        if i > max:
            max = i
    return max

nums = [1,2,3,5,3,6,1]
print(find_max(nums))