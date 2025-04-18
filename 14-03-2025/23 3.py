def f(cur,end, cnt=0):
    if cur==end: return 1
    if cur>end: return 0
    return f(cur*4,end) + \
        f(cur + 1,end) + \
        f(cur*3, end)

print(f(2,404))