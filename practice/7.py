#logical operators
n1 = int(input("enter 1st number:"))
n2 = int(input("enter 2st number:"))

print(n1>10 and n2>10)
print(n1<5 or n2<5)
print(not(n1>n2)) # first number is not greater than second number 
print("\n")

#Comparison Operator
age = int(input("enter your age:"))
if age <= 0:
    print("not valid")
elif age >= 18:
    print("your are eligible")
else:
    print("your not eligible")
print("\n")


#membership operator
Name = input("enter your name:")
print("a" in Name)
print("AN" not in Name)






    