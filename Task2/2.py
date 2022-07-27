if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=sorted(arr)
    l=[]
    for i in range(len(arr)):
        if arr[i]<max(arr):
            l.append(arr[i])
print(max(l))
