#simple greeting program using the + operator and f-string for output
name = input("enter your name:")
age = input("enter your age:")
print(f"'hello!' {name} i can not believe your {age}")
print("'hello!' " + name + " i can not believe your " + age) 

#------------------------------------------------------------------

#string manipulation exercise
user = input("what your doing:")
print(user.upper())
print(user.lower())
print(user.split())
print(user.replace(" " , "_"))

#------------------------------------------------------------------

#finding length of a string with excluding space
greet = input("hi what's your doing:")
print(len(greet.replace(' ' , '')))