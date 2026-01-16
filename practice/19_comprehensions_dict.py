# Dictionary Comprehension
students = ["Thejas", "Ragesh", "Dushyant"]
usn = [58,41,18]
dec = {name:roll for name,roll in zip(students,usn)}
print(dec)

students = ["Thejas", "Ragesh", "Dushyant"]
markes = [58,41,75]
stu ={name:mark for name,mark in zip(students,markes) if mark > 50}
print(stu)

students_mark =  {
    "Thejas":58,
    "Ragesh":41,
    "Dushyant":75
}
stu = {name:mark for name,mark in students_mark.items() if mark > 50}
print(stu)