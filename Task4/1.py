def swap_case(s):
    string_output = ''
    for i in s:
        if(i.isupper()==True):
            string_output += (i.lower())
        elif(i.islower()==True):
            string_output += (i.upper())
        else:
            string_output += i
    return string_output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)