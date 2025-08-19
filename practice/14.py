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
    

#nested if
day = "Sunday"
is_raining = False

if day == "Saturday" or day == "Sunday":
    if not is_raining:
        print("Let's visit Mysuru!")
    else:
        print("It's raining, let's stay home.")
else:
    print("It's a weekday, let's wait for the weekend.")    

# match-case
bat =int(input("enter your battery percentage:"))
match bat:
      case _ if bat>=80:
            print("it's good to take device outside")
      case _ if bat>=50:
            print("it's good to take charger with you")      
      case _ if bat>=30:
             print("recommend to charge before you go outside")
      case _:
            print("please charge")   