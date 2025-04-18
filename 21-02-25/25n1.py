from itertools import product

ans = []
for r in range(4):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for v in'0123456789':
            num = int(f'85{z}16{v}4')
            if num <= 10 ** 9 and num % 2658 == 0:
                ans.append([num, num // 2658])

ans = sorted(ans)
for i in ans:
    print(*i)