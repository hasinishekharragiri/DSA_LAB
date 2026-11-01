
size = 10

chain = [[] for _ in range(size)]
linear = [None] * size
quadratic = [None] * size

n = int(input("Enter number of elements: "))
keys = []

for i in range(n):
    keys.append(int(input("Enter value: ")))

# Separate Chaining
for key in keys:
    chain[key % size].append(key)

# Linear Probing
for key in keys:
    index = key % size

    while linear[index] is not None:
        index = (index + 1) % size

    linear[index] = key

# Quadratic Probing
for key in keys:
    index = key % size
    i = 0

    while quadratic[(index + i * i) % size] is not None:
        i += 1

        if i == size:
            print("Cannot insert:", key)
            break
    else:
        quadratic[(index + i * i) % size] = key

print("\nSeparate Chaining:")
for i in range(size):
    print(i, ":", chain[i])

print("\nLinear Probing:")
for i in range(size):
    print(i, ":", linear[i])

print("\nQuadratic Probing:")
for i in range(size):
    print(i, ":", quadratic[i])

