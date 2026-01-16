#sum using for loop
num = [4,2,76,234,236,875]
total = 0
for i in num:
    total = total + i
print(total)

#doubling a number 
num = [4,2,76,234,236,875]
dob = []
for i in num:
    dob.append(i*2)
print(dob)    


# Loops in dictionary 
students = {
    "thejas":58,
    "dushyant":19,
    "ragesh":41
}

for name, usn in students.items():  #we can also use .values() when we don't want keys
    print(f"{name} - {usn}")   


#for loop with range
student = ["thejas","ragesh", "dusyhant"]
markes = [85,60,90]
students = {}
for i in range(len(student)):
    students[student[i]] = markes[i]
print(students) 