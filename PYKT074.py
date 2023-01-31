for t in range(int(input())):
    list = [i for i in input().split()]
    cout = 0
    for i in list:
        if cout + len(i) > 100:
            break
        print(i, end = ' ') 
        cout +=  len(i)
        cout += 1
    print()

