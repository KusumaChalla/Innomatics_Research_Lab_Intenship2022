import numpy
N = int(input()) 

A = numpy.array([input().split() for i in range(N)], float)

print(round(numpy.linalg.det(A),2))