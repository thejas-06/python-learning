# repetition
print("who are you: ")
print((" i am a robot;\n")*2) 

# string methods

message = " i am a robot; "
print(message.upper()) # converts to capital letter  
print(message.lower()) # converts to lowercase
print(message.strip()) # Remove spaces from a string
print(message.replace("a " , "not ")) # It replaces older string by new string

# Using double quotes inside single quotes
message = " 'hello' i am a robot; "
print(message)

# Using single quotes inside double quotes
message = ' "hello" i am a robot; '
print(message)

# Triple quotes (''' or """) let you store multi-line strings
message = '''  "hello" i am robot
    who are you '''
print(message)


#Finding length of a string 
print(len(message))

# Accessing string 
print(message[3])  # first character is 0
print(message[-4]) # Start counting from end (first -1)

# String slicing 
print(message[3:8])    # 3 where is start , 8 ending + 1
print(message[25:])    # from character 25 to end
print(message[:20])    # start to character 20
print(message[::3])    # Start to end and skip Three character