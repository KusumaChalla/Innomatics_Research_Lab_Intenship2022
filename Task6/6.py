import numpy
a = numpy.eye(*map(int,input().split()))
print(str(a).replace('1',' 1').replace('0',' 0'))
