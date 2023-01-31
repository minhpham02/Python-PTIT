from math import gcd
class PhanSo:
    def __init__(selt, list):
        selt.tu = int(list[0])
        selt.mau = int(list[1])

    def RutGon(selt):
        GCD = gcd(selt.tu,selt.mau)
        selt.tu //= GCD 
        selt.mau //= GCD
    def __str__(selt):
        return f'{selt.tu}/{selt.mau}'


PS = PhanSo(input().split())
PS.RutGon()
print(PS)