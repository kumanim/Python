pystore=open('/home/ubuntu/python/cloned.txt','r')
count = 0
for i in pystore:
    count += 1
    if i.startswith('writing'):
        print(i)
    else: print ('no matching content found',count)

#keyword finding
pystore=open('/home/ubuntu/python/cloned.txt','r')
count=0
for i in pystore:
    count += 1
    i=i.rstrip()
    if 'writing' in i:
        print('keyword found in line',count, i)



