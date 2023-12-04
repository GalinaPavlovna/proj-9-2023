q = int(input("введите число 1: "))
w = int(input("введите число 2: "))
e = int(input("введите число 3: "))
r = int(input("введите число 4: "))
t = int(input("введите число 5: "))
y = int(input("введите число 6: "))
u = input("введите цвет чёрный,красный,синий: ")

if u == 'чёрный':
    u = 0, 0, 0
if u == "красный":
    u = 255, 0, 0
if u == "синий":
    u = 0, 0, 250
else:
    u = 0, 0, 0

import random
import turtle
print(u)
v = turtle.Turtle()
turtle.colormode(255)
for x in range(100000):
    v.forward(random.randrange(q, w))
    v.left(random.randrange(e, r))
    v.right(random.randrange(t, y))
    v.color(u)
