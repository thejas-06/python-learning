#lambda function

#(lambda) (parameters): (expression)

'''A lambda function is a small anonymous function 
   that can take any number of arguments but has only one expression.'''

add=lambda x,y: x+y
print(add(5,3))

double=lambda x: x*2
print(double(5))

#-------------------------------------------------------------------

#sort the list of dictionaries by marks in descending order
students = [
    {"name": "thejas", "marks": 39},
    {"name": "theju", "marks": 56},
    {"name": "tezz", "marks": 96}
]

students.sort(key=lambda x: x['marks'], reverse=True)
print(students)

#-------------------------------------------------------------------

#transform list
def transform_list(nums_list,transform_item):
    transformed_0=transform_item(nums_list[0])
    transformed_1=transform_item(nums_list[1])
    return [transformed_0,transformed_1]

print(transform_list([2,3],lambda x: x*2))

#-------------------------------------------------------------------

#python have some built in functions that can be used with lambda functions
#map(),filter(),reduce()


#map() function is used to apply a function to all the items in an iterable
nums_list=[1,2,3]
print(list(map(lambda x: x*2,nums_list)))

#filter() function is used to filter the items from an iterable based on a condition
nums_list=[1,2,3]
print(list(filter(lambda x: x%2==0,nums_list)))