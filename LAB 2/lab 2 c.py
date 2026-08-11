def recursive_search(emp_ids, key, index):
    if index == len(emp_ids):
        return -1
    if emp_ids[index] == key:
        return index
    return recursive_search(emp_ids, key, index + 1)
#input
emp_ids = list(map(int, input("Enter employee IDs: " ).split()))
key = int(input("Enter employee ID to search: " ))
#function call
result = recursive_search(emp_ids, key, 0)
#output
if result == -1:
    print("Employee ID not found")
else:
    print("Employye ID found at index" , result)

    
