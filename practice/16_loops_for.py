# for loop
fruits = ["apple", "orange", "graphs","banana"]
for fruit in fruits:
    print(fruit)


for even in range(0,20,2):
    print(even, end="->") 
print("")    


name = "Thejas"
for letter in name:
    print(letter) 
else:
    print("all printed")    
print("")


me = "thejas"
for index, letters in enumerate(name):  #unpacking  enumerate use when we need both index and a value
    print(letters*(index+1))
print("")    


mine = {"name":"thejas" , "age":19, "usn":58}
print(mine.items())    #convert dict to list inside a tuple
for key, value in mine.items():
    print(key, "->", value)
print("")



for i in range(1 ,11):
    print(f"2 * {i}= {2*i}")    
print("")


for i in range(2,4):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print(" ")