import numpy
n,m = map(int,input().split())
list1 = []
for i in range(n):
    list1.append(list(map(int,input().split())))
    
a=numpy.array(list1) 

print(numpy.transpose(a))
print(a.flatten())