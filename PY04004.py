from math import gcd

class PhanSo:
    def __init__(self, tu=None, mau=None):
        self.tu = tu
        self.mau = mau

    def RutGon(selt):
        GCD = gcd(selt.tu,selt.mau)
        selt.tu //= GCD
        selt.mau //= GCD

    def __add__(selt, other):
        tmp = PhanSo()
        tmp.tu = selt.tu * other.mau + other.tu * selt.mau
        tmp.mau = selt.mau * other.mau
        tmp.RutGon()
        return tmp

    def __str__(selt):
        return f'{selt.tu}/{selt.mau}'

PS = [int(i) for i in input().split()]
p1 = PhanSo(PS[0], PS[1])
p2 = PhanSo(PS[2], PS[3])
tmp =  p1 + p2
print(tmp)