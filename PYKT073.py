list = [len(input().split()) for t in range(int(input()))]
res = []
i = 0
while i < len(list):
    if list[i] == 7:
        i += 4
        res += [2]
    elif list[i] == 6:
        i += 2
        res += [1]
        while i < len(list) and list[i] == 6:
            i += 2
print(len(res), *res, sep='\n') 
