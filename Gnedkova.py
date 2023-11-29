import random
s=0
t=0
while s<3 and t<3:
    a=int(input("1=камень 2=бумага 3=ножницы"))
    # 1>3, 2>1, 3>2
    b=int(random.randint(1,3))
    print(b)
    if a==b:
        s=s+0
        t=t+0
    else:
        if a==2 and b==1 or a==3 and b==2 or a==1 and b==3:
             s=s+1
             t=t+0
        if b==2 and a==1 or b==3 and a==2 or b==1 and a==3:
             s=s+0
             t=t+1
    print("ваш счет", s)
    print("счет компьютера", t)
if s>t:
    print("вы победили")
else:
    print("вы проиграли")