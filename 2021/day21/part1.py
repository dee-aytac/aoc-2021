with open('sample.txt') as f:
    p1, p2 = f.read().strip().split('\n')
    p1 = int(p1[-1])
    p2 = int(p2[-1])

rolled = 0
start = 1


class Dice(object):
    def __init__(self):
        self.n = 1 
    
    def get_pos(self):
        sum_ = 0
        x =  self.n
        for i in range(x, x + 3):
            sum_ += i
            self.n += 1
        return sum_



dice = Dice()

s1 = 0
s2 = 0

while True:
    p1 += dice.get_pos()
    s1 += (p1 - 1) % 10 + 1
    rolled += 3
    if s1 >= 1000:
        print(s2 * rolled)
        break
    p2 += dice.get_pos()
    s2 += (p2 - 1) % 10 + 1
    rolled += 3
    if s2 >= 1000:
        print(s1 * rolled)
        break


