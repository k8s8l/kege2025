def f(cur,end):
    if cur==end:
        return 1
    if cur > end or cur ==30:
        return 0
    return f(cur-1,end)+f(cur//2,end)
print(f(30,1)*f(30,12))