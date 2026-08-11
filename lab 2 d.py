def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
#input
n = int(input("Enter a number: "))
#function call
result = factorial(n)
#output
print("Factorial of", n, "is", result)
