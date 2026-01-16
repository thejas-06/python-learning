#tuples
single = ("thejas",) #single tuples
print(type(single))
name = ("thejas","theju","teju")
print(name[2])
print(name[0::2])

#tuple concatenation
tuple1 = ("what","your")
print("what" in tuple1) #Membership
tuple2 = ("name",)
print(tuple1+tuple2) 

#tuple repetition
tuple = (1,2)*2
print(tuple)

#tuple methods
number = (1,2,2,1,3,4)
print(number.count(2)) 

print(number.index(1)) #it will return the first index of the element
print(number.index(1,2)) #it will return the index of the element starting from the given index(value, start)
print(number.index(1,2,4)) #it will return the index of the element starting from the given index(value, start, end)