
from random import randint
import sys
from draw import tick, start
from zver import Zver

zveri = []
pole = []
WIDTH = 1000
HIGH = 800

for i in range(HIGH):
    ryad = []
    for o in range(WIDTH):
        if i > 300 and i < 500:
            ryad.append({'eda': 100, 'zver': 0})
        else:
            ryad.append({'eda': 0, 'zver': 0})
    pole.append(ryad)

for i in range(2000):
    z = Zver()
    zveri.append(z)

start(zveri)

while 1:
    for i in zveri:
        try:
            pole[i.y][i.x]['eda'] -= 10 if pole[i.y][i.x]['eda']>=10 else 0
        except:
            pass
        i.pol(pole)
        if i.gl <= 0:
            zveri.remove(i)
    tick(zveri, pole)