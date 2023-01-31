class Receipts:
    def __init__(self, id, name, old_parameter, new_parameter):
        self.id = id
        self.name = name
        self.old_parameter = old_parameter
        self.new_parameter = new_parameter
        self.calculate()
    
    def calculate(self):
        self.total = self.new_parameter - self.old_parameter
        self.price = 0
        if self.total <= 50:    
            self.price = self.total * 102
        elif self.total <= 100:
            self.price = 50*100 + (self.total-50)*150
            self.price *= 1.03
        else:
            self.price = 50*100 + 50*150 + (self.total-100)*200
            self.price *= 1.05
        self.price = round(self.price)
    
    def __str__(self):
        return self.id + " " + self.name + " " + str(self.price)

receipts = []
for t in range(int(input())):
    receipts += [Receipts('KH{0:0>2}'.format(t+1), input(), int(input()), int(input()))]
receipts.sort(key=lambda ele: -ele.price)
print(*receipts, sep = '\n')