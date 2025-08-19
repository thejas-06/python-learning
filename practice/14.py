#Conditional Statements
battery =int(input("enter your battery percentage:"))
if battery>=80:
    print("it's good to take device outside")
elif battery>=50:
        print("it's good to take a charger with you")
elif battery>=30:
        print("recommend to charge before you go outside")
else:
        print("please charge")
    