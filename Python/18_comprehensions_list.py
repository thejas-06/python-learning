#List Comprehension
num = [4,2,9,234,236,875]
dob = [i*2 for i in num]  #or [i**2 for i in num if i<10]
print(dob)

num = [i for i in range(11) if i%2 == 0]
print(num)
dob = [i*2 for i in num]
print(dob)

name = ["Thejas", "Ragesh", "dushyant"]
ch = [i[0]+i[-1] for i in name]
print(ch)