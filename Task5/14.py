# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
input_1 = int(input())
for i in range(input_1):

    uid_num = input()

    
    pattern1 = len(re.findall(r"[A-Z]", uid_num)) >= 2

   
    pattern2 = len(re.findall(r"[0-9]{3}", uid_num)) >= 3

    
    pattern3 = len(re.findall(r"[a-zA-Z0-9]", uid_num)) == len(uid_num)

   
    pattern4 = len(set(uid_num)) == len(uid_num)


    pattern5 = len(uid_num) == 10
    
    if all([pattern1,pattern2,pattern3,pattern4,pattern5]):
	print("Valid")
    else:
	print('Invalid')