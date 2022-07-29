def alpha_numeric_fun(s):
    for i in range(len(s)):
        if(s[i].isalnum()):
            return True
    return False
        
def alphabetical_fun(s):
    for i in range(len(s)):
        if(s[i].isalpha()):
            return True
    return False

def digits_fun(s):
    for i in range(len(s)):
        if(s[i].isdigit()):
            return True
    return False

def lowercase_fun(s):
    for i in range(len(s)):
        if(s[i].islower()):
            return True
    return False
     
def uppercase_fun(s):
    for i in range(len(s)):
        if(s[i].isupper()):
            return True
    return False

if __name__ == '__main__':
    s = input()
    alpha_numeric = alpha_numeric_fun(s)
    alphabetical = alphabetical_fun(s)
    digits = digits_fun(s)
    lowercase = lowercase_fun(s)
    uppercase = uppercase_fun(s)
    print(alpha_numeric)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)    