def mult(n):
    tmp = 1
    for i in(n):
        i = int(i)
        if i > 0:
            tmp *= i
    return tmp


for t in range(int(input())):
    str = input()
    print(mult(str))