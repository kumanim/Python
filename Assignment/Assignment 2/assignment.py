import os

path = '/home/ubuntu/python/'
os.chdir(path)

print(os.listdir())

user_in = input('Enter a file name: ')

if user_in == 'readlines':
    user_in = input('Enter the name of the file: ')
if os.path.exists(user_in):
    with open(user_in, 'r') as pystore:
        full = pystore.readlines()
        print(len(full))
        operation = input("Choose an operation:\n1. Count number of lines\n2. Find word to search\nEnter operation number: ")
        if operation == '1':
            print('Number of lines in', user_in, len(full))
        elif operation == '2':
            word_to_find = input("Enter the word to find: ")
            count = sum(1 for line in full if word_to_find in line)
            print(word_to_find, "appears",count,' times in',user_in)
        else:
            print("Invalid operation.")
else:
    print('File', user_in ,'not found.')