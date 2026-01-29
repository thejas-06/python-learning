#why we need *args and **kwargs

def tea_order(customer_name,tea_type):
    print(customer_name, "ordered a", tea_type,"tea")

tea_order("John", "green") # The function works perfectly fine but it required 2 arguments no more no less
''' tea_order("Jane", "black" , "honey")  
TypeError: tea_order() takes 2 positional arguments but 3 were given'''

#we can over come this by adding extra parameters,but

def tea_order(customer_name,tea_type,sweetener=None):
    print(customer_name, "ordered a", tea_type,"tea")
    if sweetener!=None:
        print("with", sweetener)

tea_order("John", "green")
tea_order("Jane", "black" , "honey")
#Return this way our function does accommodate Jane order
#tea_order("Jane", "black","honey", "oat") # To use this we need to add extra optional parameter to the function but it's not scalable

#----------------------------------------------------------------------------------

#that's where *args come in
#*args is a tuple of arguments
def tea_order(customer_name,tea_type,*args): #by adding *args(*) we are telling python that the function can accept any number of positional arguments
    print(customer_name, "ordered a", tea_type,"tea")
    if args:
        print("with", args)  #args is just a variable name we can use any name we want the * is what makes it special
tea_order("thejas", "green")
tea_order("teju", "black" , "honey")
tea_order("tezz", "black","honey", "cow","oat")

#----------------------------------------------------------------------------------

'''but there is one limitation with our current approach 
   when we look at tezz order we can see he wants oat 
   but does want oat milk or oat creamer in is tea
   
   the function call would be clearer if we label the arguments'''

#this is where **kwargs come in
#**kwargs is a dictionary of arguments
def tea_order(customer_name,tea_type,**kwargs): #by adding **kwargs we are telling python that the function can accept any number of keyword arguments
    print(customer_name, "ordered a", tea_type,"tea")
    for key, value in kwargs.items():
        print("  - Add", key, ":", value)
tea_order("thejas", "green") #in this case the *kwargs is an empty dictionary
tea_order("teju", "black", sweetener="honey", milk="cow")
tea_order("tezz", "black", sweetener="honey", milk="oat", creamer="oat")

#----------------------------------------------------------------------------------

"""we can also use *args and **kwargs together
  but *args should come before **kwargs"""


def tea_order(customer_name,tea_type,*args,**kwargs):
    print(customer_name, "ordered a", tea_type,"tea")
    for arg in args:
        print("  - Add",arg)
    for key, value in kwargs.items():
        print("  - Add", key, ":", value)
tea_order("thejas", "green")
tea_order("teju", "black", "honey", "cow")
tea_order("tezz", "black", sweetener="honey", milk="oat", creamer="oat")
tea_order("tejas", "green", "honey", "cow", "oat", sweetener="honey", milk="cow")
#tea_order("thejas", "green",sweetener="honey", "cow") #this will raise a TypeError because we must pass all the positional arguments before the keyword arguments

#----------------------------------------------------------------------------------

# the * operator not only used as function defintion but also in function calls

#if the particular customer is coming repeatedly we can store the extras in a tuple
thejas_extras =("honey", "cow", "oat")
# tea_order("thejas", "green", "honey", "cow", "oat") # but this is tedious
tea_order("thejas", "green", *thejas_extras) # this is more concise and convenient


thejas_extras = {"sweetener":"honey", "milk":"cow", "creamer":"oat"}
tea_order("thejas", "green", **thejas_extras)

#----------------------------------------------------------------------------------

# the * operator can be used to unpack iterables in function calls

def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers)) # this will print the sum of the numbers


def add(a, b, c):
    return a + b + c

person = {"a":1, "b":2, "c":3}
print(add(**person))

#-------------------------------------------------------------------

#Write a function called average_score that calculates the average of an arbitrary number of scores.

def average_score(*score):
    if len(score)==0:
        return 0
    average=sum(score)/len(score)
    return average
    
print(average_score(85, 90, 78))
print(average_score(100, 95))
print(average_score())

#-------------------------------------------------------------------

#Write a function describe_pet that accepts a pet’s name and type as required arguments, but can also take any number of keyword details.

def describe_pet(pet_name,animal_type,**kwargs):
    print("pet name:",pet_name)
    print("Animal type:",animal_type)
    if kwargs:
        print("Details:")
        for key, value in kwargs.items():
            print(f"    {key}:{value}")
describe_pet("Whiskers", "cat", color="gray", age=3)

#-------------------------------------------------------------------

#Write a function make_sandwich that accepts any number of ingredients and any number of optional preferences.

def make_sandwich(*ingredients,**preferences):
    print("Sandwich ingredients:")
    for ingredient in ingredients:
        print(f"    {ingredient}")
    if preferences:
        print("Preferences:")
        for key, value in preferences.items():
            print(f"    {key}:{value}")
make_sandwich("cheese", "lettuce", "tomato", spread="mayo")