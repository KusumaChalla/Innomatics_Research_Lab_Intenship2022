import numpy as np
a, b, c = map(int,input().split())
list1 =[]
list2= []
for i in range(a):
    list1.append(list(map(int,input().split())))

for i in range(b):
   list2.append(list(map(int,input().split())))
    
arrA =  np.array(list1)
arrB = np.array(list2)

print(np.concatenate((arrA, arrB), axis = 0))
