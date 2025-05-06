from turtle import *
screensize(15000,30000)
tracer(0)
m = 6
rt(45)
for i in range(10):
    rt(45)
    fd(203*m)
    rt(45)
up()
back(40*m)
rt(45)
down()
for i in range(5):
    fd(20 * m)
    lt(90)
up()
for x in range(-440, 640):
    for y in range(-640, 640):
        goto(x * m, y * m)
        dot(1, 'red')
update()
done()

