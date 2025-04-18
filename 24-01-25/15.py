def f(a):
    for x in range(1,11111):
        f=((a,x) <=(x == a)or(x==1))
        if not f:
            return False
        return True
for a in range(1,11111):
    if f(a):
        print(a)
        break


