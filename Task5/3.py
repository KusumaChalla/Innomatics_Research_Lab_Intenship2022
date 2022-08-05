# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

reg_ex = r"([a-zA-Z0-9])\1+"

result = re.search(reg_ex,input())

if result:
    print(result.group(1))
else:
    print(-1)