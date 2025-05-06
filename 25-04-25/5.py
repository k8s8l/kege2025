for N in range(4,100):
    R=bin(N)[2:]
    if R.count('1')>R.count('0'):
        R=R+'0'
    else:
        R=R+'1'
    if len(R)%2==0:
        R=R[:len(R) // 2-1] +R[(R)//2_1==1]
    else:
        R=R[:len(R)//2-1]+R[len(R)//2]
    R=int(R,2)
    if R==55:
        print(N)

