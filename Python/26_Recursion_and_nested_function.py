#iterative method
def iterative(n):
    result =1
    if n>0:
        for i in range(1,n+1):
            result=result*i
        return result
print(iterative(4))

#--------------------------------------------------------------

#Recursion is a process in which a function calls itself

#factorial
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)  #even though recursion is slow then iteration the code can be simpler and easy to write
print(factorial(5))

#---------------------------------------------------------

#finding if the number is even
def is_even(n):
    if n==0:
        return True
    if n==1:
        return False
    return is_even(n-2)
print(is_even(5))

#---------------------------------------------------------

#sum of n numbers
def sum_of_n_numbers(n):
    if n==0:
        return 0
    return n+sum_of_n_numbers(n-1)
print(sum_of_n_numbers(5))

#---------------------------------------------------------

#nested function
def outer_function(name):
    def inner_function():   #The inner function is only accessible within the outer function
        print(f"Hello, {name}!")
    inner_function()

outer_function("thejas")

#---------------------------------------------------------

def arthimatic(operation):
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract

addition = arthimatic("add")
subtraction = arthimatic("subtract")

print(addition(5, 3))
print(subtraction(5, 3))