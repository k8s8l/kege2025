from itertools import product

ans = []
for r in range(4):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
            num = int(f'124{z}5{z}79')
            if num <= 10 ** 8 and num % 22 == 0:
                ans.append([num, num // 22])

ans = sorted(ans)
for i in ans:
    print(*i)