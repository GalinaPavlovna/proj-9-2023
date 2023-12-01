from random import *


class Zver:

    def __init__(self):
        self.zhizn = True
        self.x = randint(0, 600)
        self.y = randint(0, 600)
        self.sk = randint(1, 10)
        self.np = randint(1, 4)
        self.gl = randint(1, 100)

    def napr(self):
        if self.np == 1:
            self.x = self.x + self.sk
        if self.np == 2:
            self.y = self.y + self.sk
        if self.np == 3:
            self.x = self.x - self.sk
        if self.np == 4:
            self.y = self.y - self.sk
        if self.x > 599:
            self.x = 599
            self.np = self.np + 2
        if self.x < 0:
            self.x = 0
            self.np = self.np - 2
        if self.y > 599:
            self.y = 599
            self.np = self.np + 2
        if self.y < 0:
            self.y = 0
            self.np = self.np - 2

    def glo(self, vnshn):
        if self.gl < 100:
            self.gl = self.gl + vnshn

    def rzmnz(self):
        if self.gl >= 70:
            zverzver = Zver()
            zverzver.sk = randint(self.sk - 2, self.sk + 2)
            zverzver.gl = randint(self.gl - 2, self.gl + 2)
            zverzver.x = randint(self.x - 1, self.x + 1)
            zverzver.y = randint(self.y - 1, self.y + 1)
            return zverzver

    def smert(self):
        self.gl = self.gl - randint(1, 2)

    def neumri(self, pole):
        osmotr = self.sk
        while osmotr < 3:
            try:
                c3 = pole[self.y][self.x - osmotr]['eda']
                c1 = pole[self.y][self.x + osmotr]['eda']
                c4 = pole[self.y - osmotr][self.x]['eda']
                c2 = pole[self.y + osmotr][self.x]['eda']
                c = max(c1, c2, c3, c4)
                if c1 == c2 == c3 == c4:
                    pass
                else:
                    self.np = [135, c1, c2, c3, c4].index(c)
            except:
                pass
            osmotr = osmotr + self.sk

    def pol(self, pole):
        self.napr()
        self.smert()
        self.neumri(pole)
        self.glo(pole[self.y][self.x]['eda'])
