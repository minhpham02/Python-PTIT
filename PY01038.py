def test_case():
    n = input()
    for i in range(1000):
        if int(n) % 7 == 0:
            print(n)
            return
        else:
            n = str(int(n) + int(n[::-1]))
    print("-1") 

for t in range(int(input())):
    test_case()