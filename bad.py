import os

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(os.popen('read -p "Enter a number: " var ; echo $var').read())
print(f"The factorial of {num} is {factorial(num)}")
