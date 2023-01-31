from datetime import datetime

class Receipts:
    def __init__(self, id, name, room, arrival, departure, serveFee):
        self.id = id
        self.name = name
        self.room = room
        time = datetime.strptime(departure, '%d/%m/%Y') -  datetime.strptime(arrival, '%d/%m/%Y')
        self.day = time.days + 1
        self.serveFee = serveFee

    def totalFee(self):
        if self.room[0] == '1':     return 25 * self.day + self.serveFee
        elif self.room[0] == '2':     return 34 * self.day + self.serveFee
        elif self.room[0] == '3':     return 50 * self.day + self.serveFee
        elif self.room[0] == '4':     return 80 * self.day + self.serveFee

    def __str__(self):
        return f'{self.id} {self.name} {self.room} {self.day} {self.totalFee()}'

receipts = []
for t in range(int(input())):
    receipts += [Receipts('KH{0:0>2}'.format(t+1), input().strip(), input().strip(), input().strip(), input().strip(),int(input().strip()))]
receipts.sort(key=lambda ele: -ele.totalFee())
print(*receipts, sep='\n')