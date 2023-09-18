#to write the data in csv by creating new file
import csv , os
path='/home/ubuntu/python'
os.chdir(path)
fields = ['Name', 'Occupation', 'Mode of payment', 'Destination']
#define dictionary
data = [
    {'Name': 'Ankit', 'Occupation': 'Entrepreneur', 'Mode of payment': 'Credit Card', 'Destination': 'VijaySales'},
    {'Name': 'Sharvesh', 'Occupation': 'Business', 'Mode of payment': 'Debit Card', 'Destination': 'Unicorn'},
    {'Name': 'Sajal', 'Occupation': 'Self employed', 'Mode of payment': 'UPI', 'Destination': 'Blinkit'},
    {'Name': 'Rahul', 'Occupation': 'Freelancer', 'Mode of payment': 'Credit Card', 'Destination': 'Amazon'},
]
# Open a new file called 'data.csv' for writing
with open('data.csv', 'w', newline='') as editfile:
    exec = csv.DictWriter(editfile, fieldnames=fields)
    exec.writeheader()
    for row in data:
        exec.writerow(row)
# reading the data from the file created
with open('data.csv', 'r') as file_to_read:
    data = csv.reader(file_to_read)
    for i in data:
        print(i)