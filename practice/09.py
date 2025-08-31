#list manipulation
list =[3,1,8,4,2]
print(list)

list.append(5)
print(list)

list.insert(1,6)
print(list)

list.pop(2)
print(list)

number = [3,1,2,8]
sorted_number = sorted(number , reverse=True)
print("original list:", number)
print("descending:", sorted_number)
sorted_number.reverse()
print(sorted_number)