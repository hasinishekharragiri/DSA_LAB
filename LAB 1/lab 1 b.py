def power(p, n):
    if n == 0:
        return 1
    else:
        return p * power(p, n - 1)
# Input
p = float(input("Enter the principal growth factor: "))
n = int(input("Enter the number of years: "))
# Function Call
result = power(p, n)
# Output
print("Result =", result)
