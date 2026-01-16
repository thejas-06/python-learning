#Logical operators
rain = True #rain is falling
wet = False #the ground is not wet
print(rain and wet )
print(rain or wet)
print(not rain)
print("\n")

#------------------------------------------------------

#Membership Operators (in and not in)
n1 = "thejas" 
n2 = "thejas_an"
print(("n" in n1) or ("n" in n2))
print(("n" in n1) and ("n" in n2))
print(not("n" in n1))

name = input("enter the name please:")
print(" " in name or name != "")  

age = input("are you 18+, yes or no:")
print(("yes" in age))
print("\n")

#------------------------------------------------------

#bitwise operator
a = 2 #in binary 010
b = 3 #in binary 011

# Bitwise AND
print(a & b)  

# Bitwise OR
print(a | b)  

# Bitwise XOR
print(a ^ b) 

# Bitwise NOT
print(~a)  

# Left shift
print(a << 1) 

# Right shift
print(a >> 3)  
