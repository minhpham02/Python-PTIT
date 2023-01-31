from datetime import datetime


class Biker:
    def __init__(self, name, unit, endTime):
        self.name = name
        self.unit = unit
        self.id = self.getID(name, unit)
        time = datetime.strptime(endTime, '%H:%M') - datetime.strptime('6:00', '%H:%M')
        self.speed = 120 / time.seconds * 3600

    def getID(self, name, unit):
        return ''.join([i[0:1].upper() for i in unit.split()]) + ''.join([i[0:1].upper() for i in name.split()])

    def __str__(self):
        return f'{self.id} {self.name} {self.unit} {round(self.speed)} Km/h'

list = []
for t in range(int(input())):
    list += [Biker(input(), input(), input())]
list.sort(key=lambda ele: -ele.speed)
print(*list, sep='\n')