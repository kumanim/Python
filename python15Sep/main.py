import csv,os

path='/home/ubuntu/python'
os.chdir(path)

with open('data.csv','r') as file_to_read:
    data=csv.reader(file_to_read)
    for i in data:
        print(i)