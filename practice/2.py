                        ###Swapping two numbers without a 3rd variable

# Method 1: Using arithmetic
print("whitout 3rd variable by arithmetic:")
x = 10
y = 20

x = x + y
y = x - y
x = x - y

print(x , y)

# Method 2: Python tuple unpacking (most Pythonic way)

print("whithout 3rd variable using tuple:")
p = 10
q = 20

p, q = q, p

print(p , q)

                        # Swapping two numbers with 3rd variable
print("with variable:")

a=10
b=20

temp = a
a = b
b = temp
print(a , b)