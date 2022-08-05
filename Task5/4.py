# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

constants = 'qwrtypsdfghjklzxcvbnm'

vowels = 'aeiou'

result = re.findall(r'(?<=['+constants+'])(['+vowels+']{2,})(?=['+constants+'])', input().strip(), re.IGNORECASE)

if result:
    for i in result:
        print(i)
else:
    print(-1)