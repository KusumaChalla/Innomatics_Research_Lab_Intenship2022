import numpy
coeff=list(map(float,input().split()))
a=float(input())

print(numpy.polyval(coeff,a))