# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
input_1 =int(input())

for i in range(0,input_1):
    input_2=input()

    exp=input_2.split()

    if len(exp)>1  and  '{' not in exp:
        result =re.findall(r'#[a-fA-F0-9]{3,6}',input_2)
        for  i in result:
            print(i)