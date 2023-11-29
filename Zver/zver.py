from random import randint, choice


class Zver:

    def __init__(self):
        self.zhizn = True
        self.x = randint(0, 1000)
        self.y = randint(0, 800)
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
        if self.x > 999:
            self.x = 999
            self.np = self.np + 2
        if self.x < 0:
            self.x = 0
            self.np = self.np - 2
        if self.y > 799:
            self.y = 799
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
        self.gl = self.gl - randint(1, 5)

    def neumri(self, pole):
        osmotr = self.sk
        while osmotr < 20:
            try:
                c3 = pole[self.y][self.x - osmotr]['eda']
                c1 = pole[self.y][self.x + osmotr]['eda']
                c4 = pole[self.y - osmotr][self.x]['eda']
                c2 = pole[self.y + osmotr][self.x]['eda']
                c = max(c1, c2, c3, c4)
                lst = [135, c1, c2, c3, c4]
                lst1=[]
                for i in range(5):
                    if lst[i]==c:
                        lst1.append(i)
                    self.np=choice(lst1)
            except:
                pass
            osmotr = osmotr + self.sk

    def pol(self, pole):
        self.napr()
        self.smert()
        self.neumri(pole)
        self.glo(pole[self.y][self.x]['eda'])
