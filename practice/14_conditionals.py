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

#----------------------------------------------------------------------
    

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

#--------------------------------------------------------------

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

#----------------------------------------------------------------------

battery =int(input("enter your battery percentage:"))
if battery<=100 and battery>0:
    if battery>=80:
        print("it's good to take device outside")
    elif battery>=50:
        print("it's good to take a charger with you")
    elif battery>=30:
        print("recommend to charge before you go outside")
    elif battery<30:
        print("please charge")
else:
    print("invalid input")

#----------------------------------------------------------------------

age = int(input("enter your age:"))
if age<18:
    print("you are eligible for student membership")
elif age>60:
    print("you are eligible for senior citizenship") 
else :
    print("regular plan")

#----------------------------------------------------------------------

num = int(input("enter your number:"))
if num%2==0:
    print("even")
else:
    print("odd")

#----------------------------------------------------------------------

num = int(input("enter your number:"))
if num%3==0:
    print("divisible by 3")
else:
    print("not divisible by 3")