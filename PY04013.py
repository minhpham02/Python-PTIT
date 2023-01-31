
from datetime import datetime

class Meteoglory:
    def __init__(self, id, name, timeBegin: datetime, timeEnd: datetime, amount_of_rain):
        self.id = id
        self.name = name
        self.hour = (timeEnd - timeBegin).total_seconds()/3600
        self.amount_of_rain = amount_of_rain

    def avg_of_rain(self):
        self.avg_of_rainall = self.amount_of_rain / self.hour

    def __str__(self):
        return self.id + ' ' + self.name + ' ' + '{:.2f}'.format(self.avg_of_rainall)

map_measuring = {}

stt = 1

for t in range(int(input())):
    name = input()
    newObj = Meteoglory('T{0:0>2}'.format(stt), name, datetime.strptime(input(), '%H:%M'), datetime.strptime(input(), '%H:%M'), int(input()))
    if name in map_measuring:
        map_measuring[name].hour += newObj.hour
        map_measuring[name].amount_of_rain += newObj.amount_of_rain
    else:
        map_measuring[name] = newObj
        stt += 1
for i in map_measuring:
    map_measuring[i].avg_of_rain()
    print(map_measuring[i])
