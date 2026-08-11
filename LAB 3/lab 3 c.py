def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    arr.append(num)
result = selection_sort(arr)
print("Sorted list:", result)
