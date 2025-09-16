# 1.	Write a program that takes a float number as input and prints its integer, float, and string type

num = float(input("enter any folating number:"))
print("\nWith type information:")
print(f"Integer: {int(num)} (type: {type(int(num))})")
print(f"Float: {num} (type: {type(num)})")
print(f"String: '{str(num)}' (type: {type(str(num))})")


# 2.	Enter cost of 3 items from the user (using float data type) – a pencil, a pen, and an eraser. You have to output the total cost of the items as the bill

pencil = float(input("enter the cost: "))
pen = float(input("enter the cost: "))
eraser = float(input("enter the cost: "))
print(f"total bill was:{pencil+pen+eraser}")


# 3. Take name and age as input and print: "Hello <name>, you are <age> years old

name = input("enter your name please: ")
age = int(input("enter your age: "))
print(f"\nhello {name}, your are {age} years old ")



# 4.	Write a program to count how many times a specific character appears in a string.

name = input("enter your name: ")
length =len(name.replace(" " , "")) 
print(length)


string = input()
character = input()
print(string.count(character))



# 5. Write a program to remove all spaces from a sentence

name = input("enter your name:")
print(name.replace(" " ,""))


# 6. Print the multiplication table of a number N

num = int(input("enter the number:"))
for i in range(1,11):
     print(f"{num} * {i} = {num*i}")


# 7. Print a right-angled triangle pattern with *

sym = input("enter the symbol for it:")
n = int(input("enter the number of rows:"))
for i in range(1,n+1):
    print(f"{sym*i}")


# 8. program to find the factorial of any number entered by the user

num = int(input("enter the number: "))
f = 1
for i in range(1,num+1):
    f *= i
    print(f)
print(f"factorial of {num} is {f}")    


# 9. Write a function to find the square of a number

def square(num):
    return num **2
print(square(5))
print(square(2))



#10. Write a function to calculate factorial of a number

def fac(num):
    f = 1
    for i in range(1 , num+1):
        f *=i
    return f    
print(fac(5))        


#11.Check whether a number is even or odd

num1 = int(input("enter the number:"))
if num1%2 == 0:
    print("even")
else:
    print("odd")


#12. Take 3 numbers and print the largest

def find_largest(nums):
    largest = nums[0]
    for n in nums:
        if n > largest:
            largest = n
    return largest

nums = [24, 4, 10]
print(f"{find_largest(nums)} is largest")
