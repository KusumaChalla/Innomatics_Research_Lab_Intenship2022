# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
input_num = int(input())
for i in range(input_num):
    input2 = input()
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$',input2)))