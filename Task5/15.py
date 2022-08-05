import re
input_1 = int(input())
for i in range(input_1):
    pattern = r"[456]\d{3}(-?\d{4}){3}$"
    input_2 = input()
    if bool(re.match(pattern, input_2)) is True:
        if bool(re.search(r"([\d])\1\1\1", input_2.replace("-", ""))) is False:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")