#list =[5,8,3,33,9,11]

#def sq_n_c(n):
#    print(n*n)
 #   print(n*n*n)

#for i in list:
#    (sq_n_c(i))
'''
random =[5,8,3,4,9,11]
def sq_fn(n):
    print(n*n)

squares=list(map(sq_fn,random))

def c_fn(n):
    print(n*n*n)

cubes=list(map(c_fn,random))

# Create a list of tuples where each tuple contains (name, score)
students = [
    ("Alice", 90),
    ("Bob", 75),
    ("Charlie", 60),
    ("David", 85),
]
# Define functions for filtering
def distinction_class(score):
    return score > 80
def first_class(score):
    return 65 < score <= 80
def just_passed(score):
    return score <= 65
# Filter individuals based on the criteria
distinction_students = [name for name, score in students if distinction_class(score)]
first_class_students = [name for name, score in students if first_class(score)]
just_passed_students = [name for name, score in students if just_passed(score)]
# Print the results
for student in distinction_students:
    print(f"{student} has been awarded distinction class.")
for student in first_class_students:
    print(f"{student} has been awarded first class.")
for student in just_passed_students:
    print(f"{student} has just passed.")


sq_fn =lambda n : print(n**2, 'is the square of', n)
#invokation
sq_fn(39)

#declare
sq_fn = lambda n : n*n

sq_fn = lambda n : print(n*n)

sq_fn = lambda n : print(n*n, 'is the square of', n)

#invokation
sq_fn(11)

scores=[80,75,90,65,50,45,99,81]

ftr = lambda n : n>80

ftr = lambda n : print(n, 'has distinction') if (n>80) else { print(n, 'has top class') if (60< n <80)else None}

toppers=list(filter(ftr,scores))
toppers

val1 = int(input('Enter the first numerical: '))
val2 = int(input('Enter the second numerical: '))

sum = val1+val2
print(sum)

Name= str(input('Please enter your first name: '))

print('Hello', Name.capitalize(), '!')

val1 = int(input('Enter the first numerical: '))
val2 = int(input('Enter the second numerical: '))

sum = val1+val2
sub = val1-val2
mul = val1*val2
div = val1/val2
print(sum,sub,mul,div)

val1 = int(input('Enter the first numerical: '))
val2 = int(input('Enter the second numerical: '))

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    result = val1 + val2
    operation = "addition"
elif choice == '2':
    result = val1 - val2
    operation = "subtraction"
elif choice == '3':
    result = val1 * val2
    operation = "multiplication"
elif choice == '4':
    if val2 != 0:
        result = val1 / val2
        operation = "division"
    else:
        result = "Division by zero is not allowed."
        operation = "division"
else:
    result = "Invalid choice"
    operation = "N/A"

print("Result of " + operation + ": " + str(result))

method =('Please specify an operation : ')

if method.lower == 'div':
    try:
        div=v1/v2
    except:
        print('Please provide a positive integer for division')


psy=open('/home/ubuntu/python/cloned.txt','a')
line1=psy.readline()
print(line1)
'''

pystore=open('/home/ubuntu/python/cloned.txt','a')
pystore.write('\n writing new stuff interactively!. \n')
pystore.close()

pystore=open('/home/ubuntu/python/cloned.txt','r')
sentence=pystore.readline()
while (sentence!=""):
    print(sentence)
    sentence=pystore.readline()


