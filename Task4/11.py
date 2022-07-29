def print_rangoli(size):
    # your code goes here
    string = "abcdefghijklmnopqrstuvwxyz"
    data = [string[i] for i in range(n)]
    sentence = list(range(n))
    sentence = sentence[:-1]+sentence[::-1]
    for i in sentence:
        var = data[-(i+1):]
        row_n = var[::-1]+var[1:]
        print("-".join(row_n).center(n*4-3, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)