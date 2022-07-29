# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = int(input())
BC = int(input())

AC = math.sqrt(AB**2 + BC**2)
MB = AC/2
adjacent_line = BC/2

angle = int(round(math.degrees(math.acos(adjacent_line/MB))))
angle = str(angle)
print(angle+'\u00B0')