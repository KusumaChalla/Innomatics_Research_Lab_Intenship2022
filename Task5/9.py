# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = r'^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$'
input_ = int(input())
for i in range(input_):
    
    name, email = input().split(' ')
    
    if re.match(pattern, email):
        print(name, email)