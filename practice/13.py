#Dictionaries
student1 = {
    "name" : "Thejas AN",
    "USN" : "4MH23CA001",
    "sem": 5
}

student2 = {
    "name" : "dushyant",
    "USN" : "4MH23CA002",
    "sem" : 5.0
}

#accessing dictionary elements
print(student1["name"])
print(student2.get("name"))
print(student1.get("college" , "not found"))  #using get() it do not give error 
