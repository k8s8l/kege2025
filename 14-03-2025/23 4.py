def f(cur, cnt=0):
    if cnt == 13 and cur < 0:
        ans.append(cur)
        return 1
    if cnt == 13 and cur >= 0:
        return 0
    return f(cur - 3, cnt + 1) + f(cur * (-3), cnt + 1)

def g(cur, cnt=0):
    if cnt == 13 and cur < 0:
        return {cur}
    if cnt == 13 and cur >= 0:
        return set()
    return g(cur - 3, cnt + 1) | g(cur * (-3), cnt + 1)

ans = []
print(f(333), len(set(ans)))

print(len(g(333)))