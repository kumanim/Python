#read the file using import os

import os
path='/home/ubuntu/python/'
os.chdir(path)


print(os.listdir())

user_in=input('Enter a file name: ')
pystore=open(user_in,'r')