#   Functions Declaration

def function_name(argument):
    print(argument)

def print_h1(name):
    print('hi', name)

#   Invoke
if 1>0:
    print_h1('Pycharm')
else:
    function_name('IDE')


print_h1('Zing')
function_name('zen')
print_h1('Zarin')
def function_compare(argument):
    print(argument)
# Invoke
# #It will run the comparison operation and is Boolean value
if 2==2:
    function_compare('It\'s a match!')
else:
    function_compare('Not a match!')

obj1="NatWest"
obj2="RBS"
obj3="Natwest"

if obj1==obj2:
    print('it is not a match')
elif obj1==obj3:
    print('It is a match')
else:
    print('Not a match')

print(obj1, "it's a match", obj3)

def cmp(n1,n2):
    if n1 > n2:
        print(n1, 'is greater than',n2)


# User defind method to find square
# Define the first dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3}
# Define the second dictionary
dict2 = {'a': 1, 'b': 2, 'c': 3}
# Compare the dictionaries
if dict1 == dict2:
    print("Dictionaries have the same content which is", dict1)
else:
    print("Not similar")

#task5
scores=[90,95,80,76,91,82]
for i in scores:
    if i > 80:
        print(i)
scores={'rohit':90, 'vishal':80, 'jack':76, 'jenny':82}
for i in scores:
    print(i, 'has scored', scores[i])

for student, score in scores.items():
    if score > 80:
        print(f'{student} has been awarded distinction class')
    elif score > 65 and score <= 80:
        print(f'{student} has been awarded first class')
    else:
        print(f'{student} has just passed')

#Task3
n = 2
square = n ** 2
cube = n ** 3
print("\nSquare of the number :-->", square)
print("Cube of the number :-->", cube)


#Task4
import math
def square_root(number):
    if number >= 0:
        result = math.sqrt(number)
        print(f"Square root of {number} is: {result}")
    else:
        print("Cannot compute the square root of a negative number.")
square_root(25)

#Tasksqaure
list =[5,8,3,33,9,11]

def sq_n_c(n):
    print(n*n)
    print(n*n*n)

for i in list:
    (sq_n_c(i))