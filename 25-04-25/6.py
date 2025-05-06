from turtle import *
tracer(0)
m = 2
rt(-90)

for i in range(2):
    fd(5 * m)
    rt(90)
    fd(11 * m)
    rt(90)
up()
fd(-4 * m)
rt(90)
fd(6 * m)
lt(90)
down()
for i in range(2):
    fd(42 * m)
    rt(90)
    fd(63 * m)
    rt(90)
up()
for x in range(-60, 60):
    for y in range(-60, 60):
        goto(x * m, y * m)
        dot(3, 'white')

