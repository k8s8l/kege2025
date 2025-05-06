print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f= (w>=(y==z))  and (y==(z>=x))
                if f:
                    print(w, x, y, z)
