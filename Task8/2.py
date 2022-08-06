def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def binom(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

p, n = list(map(int, input().split(" ")))
print(round(sum([binom(i, n, p/100) for i in range(3)]), 3))
print(round(sum([binom(i, n, p/100) for i in range(2, n+1)]), 3))