kri = [1]*10
for i  in range(2,10):
    kri[i] = kri[i-1]*i

for case in range(int(input())):
    n = input()
    s = sum(kri[int(i)] for i in n)
    print('Yes' if s == int(n) else 'No')


