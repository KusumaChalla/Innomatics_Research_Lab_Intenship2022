import numpy
n,m=map(int,input().split())

array= [list(map(int,input().split())) for i in range(n)]

print(numpy.prod(numpy.sum(array,axis=0),None))