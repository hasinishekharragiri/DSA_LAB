def countdown(n):
    if n == 0:
        print("Launch!")
    else:
        print(n)
        countdown(n - 1)
# Input
n = int(input("Enter the countdown number: "))
# Function Call
countdown(n)
