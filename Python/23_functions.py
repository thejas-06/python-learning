#function without parameter
def greet():
    print(f"hello! nice to meet you")
greet()

#---------------------------------------------------

#function with parameter
def greet(name):
    print(f"hello! {name} nice to meet you")

greet("thejas") #positional arguments
greet("dushyanth")
greet("teju")
greet(name="tezz") #keyword arguments

#---------------------------------------------------

# mix of positional arguments and keyword arguments

# Old function
def old_function(x, y):
    return x + y

# New version with extra features
def new_function(x, y, multiplier=1):  #default parameter values
    result = (x + y) * multiplier
    return round(result)

print(old_function(5, 3))        # 8 old function
print(new_function(5, 3))        # 8 (same) still workes
print(new_function(5, 3, multiplier=2))  # 16  mix of both

#----------------------------------------------------------

def table(num):
    for i in range(1,11):
        print(f"{num}x{i} = {num*i}")
table(2)
table(3)

#-----------------------------------------------------------

def calc_rect_area(length,width):
    area=length*width
    return area   # without this the python gives an error because the variable within the function python stores in the local variable

area=calc_rect_area(14,10)  # To keep using the return value in rest of our program we need to capture in a variable
unit="feet square"
print(area, unit) 

#---------------------------------------------------------

def compute(a, b):
    result = a * b
    if result > 10:
        return result - 3
    return result + 4

print(compute(3, 2))
print(compute(5, 3))