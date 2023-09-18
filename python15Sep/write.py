import csv,os

path='/home/ubuntu/python'
os.chdir(path)

fields=['Name','Occupation','Mode of payment','Destination']

recs=[
    ['Jack','Enterprenur','credit card','Croma'],
    ['Som','Business','Debit Card','Unicorn'],
    ['Seema','Selfemployed','UPI', 'Amazon'],
    ['Shalini','Freelancer','credit Card','flipkart']
]

with open('spends.csv','w') as editfile:
    exec=csv.writer(editfile)
    exec.writerow(fields)
    exec.writerows(recs)

with open('spends.csv','r') as file_to_read:
    data=csv.reader(file_to_read)
    for i in data:
        print(i)