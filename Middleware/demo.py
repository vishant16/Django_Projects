#a=[i*i for i in range(100) if i%2==0 ]
#print(a)


es=[]
for i in range(100):
    if i%2==0:
        es.append(i*i)

print(es)
