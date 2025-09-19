
                                                                     #string
# 1. Count vowels a string

st = input("enter any string: ").lower()
vowels = "aeiou"
vowel_count = 0

for i in st:
    if i in vowels:
        vowel_count += 1

print("vowels:", vowel_count)

           #or
text = input("enter any string: ").lower()
vowels = "aeiou"
vowel_count = 0

for v in vowels:
    vowel_count += text.count(v)

print("Vowels:", vowel_count)


#2. Remove all duplicate characters from a string
 
text = input("enter the string: ")
result = ""

for i in text:  
    if i not in result:  # only add if it's not already included
        result += i

print("Result:", result)

          #or

text = input("enter the string: ")
result = "".join(dict.fromkeys(text)) #creates a dictionary with characters as keys
print(dict.fromkeys(text))
print("Result:", result)


# 3. Find the longest word in a sentence

sentence = "I love programming in Python"
words = sentence.split()   
longest = ""               

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

                  #or

sentence = "I love programming in Python"
words = sentence.split()

longest = max(words)  

print("Longest word:", longest)




                                                                     #loops

#4. Print a diamond pattern with *
n = 4
for i in range(-n+1, n):
    spaces = abs(i)
    stars = 2*(n - abs(i)) - 1
    print(" " * spaces + "*" * stars)



# 5. Reverse the digits of a number using a loop
num = input("enter any number:")
reverse = num[::-1]      
print("Reversed:", reverse)

#        or 

num = input("enter any number:")
reverse = ""

for i in num:
    reverse = i + reverse   

print("Reversed:", reverse)


# 6. Generate the Fibonacci sequence up to N terms

n = 7
a, b = 0, 1   
print(a, b, end=" ")

for _ in range(2, n):  # start from 2 since 0 and 1 are already printed
    c = a + b
    print(c, end=" ")
    a, b = b, c

