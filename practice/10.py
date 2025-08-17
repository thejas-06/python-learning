#tuples
single = ("thejas",) #single tuples
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
number = (1,2,1,2,3,4)
print(number.count(2)) 

print(number.index(1))