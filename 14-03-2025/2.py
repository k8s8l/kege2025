print('x','y','z','w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f=(z<=x)==(w<=y)or(x and w)
                if not f:
                    print(x,y,z,w)
#xwyz

