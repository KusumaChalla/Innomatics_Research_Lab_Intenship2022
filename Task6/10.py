import numpy
n,m=map(int,input().split())

list1 = [list(map(int,input().split())) for i in range(n)]

arr = numpy.array(list1)

print(max(numpy.min(arr,axis=1)))