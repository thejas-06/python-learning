#sets
number = {1,} #single set
print(type(number))
print(number)

empty_set = set() #empty set do not leave like set = {}

#set operations
set1 = {1,2,3}
set2 = {3,4,5}
print(set1 | set2) #union operation
print(set1 & set2) #intersection operation
print(set1 - set2) #difference
print(set2 - set1) #difference
print(set1 ^ set2) #symmetric difference

#set methods
set = {"apple", "orange"}
print(set)

set.add("thejas") #add at random position
print(set)

set.remove("thejas")
print(set)

set.discard("teju") # set.remove("teju") this comes typeerror when we try to delete what not in set
print(set)

print(set.pop()) # it pop random element

set.clear()
print(set)