n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    arr.append(num)
key = int(input("Enter element to search: "))
# Linear Search
found = False
for i in range(n):
    if arr[i] == key:
        print("Element found at index", i)
        found = True
        break
if found == False:
    print("Element not found")
