pystore=open('/home/ubuntu/python/cloned.txt','r')
full=pystore.readlines()
print(full)

#lines using for loop

pystore=open('/home/ubuntu/python/cloned.txt','r')
count=0

for i in pystore:
    count+=1

print(count)
print(type(pystore))