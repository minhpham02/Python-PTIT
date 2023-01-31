from math import gcd

class PhanSo:
    def __init__(self, tu = None, mau = None):
        self.tu = tu
        self.mau = mau

    def RutGon(self):
        GCD = gcd(self.tu,self.mau)
        self.tu //= GCD
        self.mau //= GCD

    def __add__(self, other):
        tmp = PhanSo()
        tmp.tu = self.tu * other.mau + other.tu * self.mau
        tmp.mau = self.mau * other.mau
        tmp.RutGon()
        return tmp    

    def __str__(self):
        return f'{self.tu}/{self.mau}'

PS = [int (i) for i in input().split()]
PS1 = PhanSo(PS[0], PS[1])
PS2 = PhanSo(PS[2], PS[3])
tmp = PS1 + PS2
print(tmp)