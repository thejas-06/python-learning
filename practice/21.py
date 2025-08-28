# Splitting Strings to Create Lists
name = "my name is thejas"  
spl = name.split()    #try to convert to list
print(spl)

name = "my-name-is-thejas"  
spl = name.split("-")    #try to convert to list
print(spl)


integer = input("enter the number of integer: ").split()
inte = [int(i) for i in integer]
print(inte)