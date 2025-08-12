boy_name = input("enter the boy name: ") 
boy_age = int(input("enter the boy age: ")) #here it always take it as a string that's why we need to convert in to int

girl_name = input("enter the girl name: ")
girl_age = int(input("enter the girl age: "))

# here i use abs because sometime boy might be younger 
age_difference = abs(boy_age - girl_age)

print(boy_name + " loves " + girl_name + " and the age difference is " + str(age_difference) )  # String concatenation 

print(f"{boy_name} loves {girl_name} and the age difference is {age_difference}")  #string formate