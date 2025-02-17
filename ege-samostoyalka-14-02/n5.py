ans=[]
for n in range(0,10000):
    r=bin(n)[2:]
    if len(r)%3==0:
        r=r+r[-3:]
    else:
        r=r + bin(n%3*3)[2:0]
        r=int(r,10)
        if r<170:
            ans.append(r)
print(max(ans))


