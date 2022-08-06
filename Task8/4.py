import math
mean, std = 70, 10
spf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))


print(round((1-spf(80))*100,2))
print(round((1-spf(60))*100,2))
print(round((spf(60))*100,2))