from turtle import*
tracer(0)
m=6
rt(-90)

for i in range(9):
    fd(15*m)
    rt(90)
    fd(25*m)
    rt(90)
up()
back(10*m)
rt(90)
down()
for i in range(8):
    fd(15*m)
    lt(90)
    fd(25*m)
    lt(90)
up()
fd(6*m)
lt(90)
down()
for i in range(7):
    fd(15*m)
    rt(90)
    fd(25*m)
    rt(90)
up()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*m,y*m)
        dot(3,'red')
update()