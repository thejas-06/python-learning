#tuple
tuple1 = (1,7,4,9,3)
print(tuple1[1:3])
tuple2 = (3,5,2)
tuple0 = tuple1+tuple2
print(tuple0)

#set
set1 = {"apple","orange","banana","green_apple"}
set2 = {"apple", "Pomegranate", "Strawberry"}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
set1.add("Pomegranate")
print(set1)

set1.remove("green_apple")
print(set1)

set1.discard("green_apple")
print(set1)


my_list = [1,2,3,4,5]
my_tuple = tuple(my_list)
print(my_tuple)
my_set = set(my_list)
print(my_set)
my_set.add("9")
print(my_set)
