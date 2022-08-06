import numpy as np
n, m = map(int, input().split())

a= np.array([list(map(int,input().split())) for i in range(n)])
print(np.mean(a,axis=1))
print(np.var(a,axis=0))
print(np.round(np.std(a),11))