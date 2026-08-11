n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    arr.append(num)
# Sort the list
arr.sort()
print("Sorted list:", arr)
key = int(input("Enter element to search: "))
# Binary Search
low = 0
high = n - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("Element found at index", mid)
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")
