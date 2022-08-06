# Enter your code here. Read input from STDIN. Print output to STDOUT
#Factorial function

def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def combine(n, x):
    return fact(n) / (fact(x) * fact(n-x))

#binomial function 

def binom(x, n, p):
    return combine(n, x) * p**x * (1-p)**(n-x)

children, boy = list(map(float, input().split(" ")))

#To calculate the probability of boy

prop = children / boy 

#sum the probabilities of 3,4,5 or 6 boys

print(round(sum([binom(i, 6, prop / (1 + prop)) for i in range(3, 7)]), 3))