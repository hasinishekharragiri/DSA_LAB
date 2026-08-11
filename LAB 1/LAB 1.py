#1 Example about comments
number1 = 10      # stores 1st value and its key
number2 = 15      # stores 2nd value and its key
sum = number1 + number2      # adds 1,2 in name of sum
product = number1 * number2  # multiplies 1,2 in name of product
print("The sum is :", sum)
print("The product is :", product)


#2 Changing the value of a variable in Python
site_name = "programiz.pro"
print(site_name)
   # now assign new value to site_name
site_name = "apple.com"
print(site_name)


#3 Addition of string and integer using Explicit Conversion
num_string = "12"
num_integer = 23
print("Data type of num_string before Type Casting:",
      type(num_string))
# explicit type conversion
num_string = int(num_string)
print("Data type of num_string after Type Casting:",
      type(num_string))
num_sum = num_integer + num_string
print("Sum:", num_sum)
print("Data type of num_sum:", type(num_sum))


#4 Arithmetic operators in Python
a = 7
b = 2
print("Sum:", a + b)                   # add
print("Subtraction:", a - b)           # subtraction
print("Multiplication:", a * b)        # multiplication
print("Division:", a / b)              # division
print("Floor Division:", a // b)       # floor division
print("Modulo:", a % b)                # modulo division
print("Power:", a ** b)                # a to the power b


#5 Assignment Operators
a = 10
b = 5
a = a + b
a += b
a -= b
print(a)


#6 Comparison Operators
a = 5
b = 2
print(a == b)   # equal to
print(a != b)   # not equal to
print(a > b)    # greater than
print(a < b)    # less than
print(a >= b)   # greater than or equal to
print(a <= b)   # less than or equal to


#7 Logical Operators
# Logical AND
print(True and True)
print(True and False)
# Logical OR
print(True or False)
# Logical NOT
print(not True)


#8 Identity Operators in Python
x1 = 5
y1 = 5
x2 = "Hello"
y2 = "Hello"
x3 = [1, 2, 3]
y3 = [1, 2, 3]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)


#9 Membership Operators in Python
message = "Hello world"
dict1 = {"a": 1, "b": 2}
# check if 'H' is present in message string
print("H" in message)
# check if 'hello' is present in message string
print("hello" not in message)
# check if 'a' key is present in dict1
print("a" in dict1)
# check if 'c' key is present in dict1
print("c" in dict1)
