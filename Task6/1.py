import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr.reverse()
    a = numpy.array(arr,float)
    return a

arr = input().strip().split(' ')
result = arrays(arr)
print(result)