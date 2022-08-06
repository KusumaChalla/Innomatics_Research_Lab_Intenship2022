import numpy
n,m = map(int,input().split())
a = numpy.array([input().split() for i in range(n)],int)
b = numpy.array([input().split() for i in range(n)],int)
print(a+b,a-b,a*b,a//b,a%b,a**b,sep="\n")