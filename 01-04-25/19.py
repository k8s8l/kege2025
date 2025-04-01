def f(k_1, k_2,m):
    if k_1 + k_2 >= 65:
        return m % 2 ==0
    if m==0:
        return
    h=[f(k_1+1, k_2, m-1),
       f(k_1*3, k_2, m-1),
       f(k_1, k_2+1, m-1),
       f(k_1, k_2*3, m-1)]
    return any(h) if (m-1)%2==+0 else all(h)
print('19',[m for m in range(1,59) if f(m,6,2)])


