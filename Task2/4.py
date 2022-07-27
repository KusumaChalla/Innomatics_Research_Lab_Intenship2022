if __name__ == '__main__':
    N = int(input())
    operation=[]
    for i in range(N):
        operation.append(input().split())

    result=[]
    for i in range(N):
        if operation[i][0]=='insert':
            result.insert(int(operation[i][1]),int(operation[i][2]))
        elif operation[i][0]=='print':
            print(result)
        elif operation[i][0]=='remove':
            result.remove(int(operation[i][1]))
        elif operation[i][0]=='append':
            result.append(int(operation[i][1]))
        elif operation[i][0]=='sort':
            result.sort()
        elif operation[i][0]=='pop':
            result.pop()
        elif operation[i][0]=='reverse':
            result.reverse()
                        