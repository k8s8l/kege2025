from itertools import product

ans = []
for A in '02468':
    for i in range(4):
        for B in product('13579', repeat=i):
            B = ''.join(B)
            num = int('1' + A + '2157' + B + '4')
            if num % 133 == 0:
                ans.append([num, num // 133])

ans = sorted(ans)
for i in ans:
    print(*i)