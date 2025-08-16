#lists
iteam = [1, "name", True] #list can hold any datatype

#accessing list
iteam = ["thejas", "teju", "tejas"]
print(iteam[0])
print(iteam[-1])
print("\n")

    #modifying a list
# Changing a specific elememt
iteam[0] = "Thejas" 
print(iteam)

# adding a element 
iteam.append("tezz") # adding a element at the end 
print(iteam)

iteam.insert(0, "Tezz") # Adding a element at specific position 
print(iteam)
print("\n")

#removing element
iteam.remove("Tezz")
print(iteam)
 
iteam.pop() # Remove the element at the end 
print(iteam)

iteam.pop(2) # Remove element at a specific position 
print(iteam)

iteam.clear()
print(iteam) # it delete entire list or all element 
print("\n")

#slicing list
iteam = ["a","b","c","d"]
print(iteam[0:2]) #print a and b
print(iteam[1:])
print(iteam[0::2]) # It prints a and c
iteam2 = iteam[0:2]
print(iteam2)
print("\n")

#functions
number = [5,6,3,8,1]
print(len(number))

print(sorted(number)) 

add = sum(number)
print(add)
print("\n")

#methods
fruits = ["banana", "apple", "orange"]
print(fruits.index("orange"))

count = [1,2,3,2,2]
print(count.count(2))

fruits.reverse() # We can not make separate list Using this 
print(fruits)

count.sort() #We can not make separate list Using this 
print(count)
print("\n")

#nested list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][1]) # This means in the first list i want the Index one element(2nd element)
print(matrix[2][2])

