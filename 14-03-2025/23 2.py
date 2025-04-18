def f(cur, end, B=False):
    if cur == end: return 1
    if cur > end: return 0
    if B:
        return f(cur + 2, end) + f(cur * 3, end)
    return f(cur + 2, end) + f(cur ** 2, end, True) + f(cur * 3, end)


print(f(2, 64))
