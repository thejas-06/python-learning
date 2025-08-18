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

#adding element to dictionaries
student1["college"] = "MIT"
student2["college"] = "MIT"
print(student1)
print(student2)

#updating
student2["college"] = "VV"
print(student2)

#removing element
student1.pop("college")
print(student1)
del student2["college"]
print(student2)

# student1.clear() 


#Dictionary methods
print(student1.keys())  #it prints all dictionary keys
print(student1.values()) #it prints all dictionary values
print(student1.items())  # Returns key-value pairs as tuples

new_update = {"branch" : "AI"}
student1.update(new_update)