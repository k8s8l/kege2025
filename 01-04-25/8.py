from itertools import product
alph=('лунатик')
alph=sorted(alph)
glas=('уаи')
last_pos=0
for pos,val in enumerate(product(alph, repeat = 6), start=1):
    val="".join (val)
    if val[0] =='' and val.count('у') + val.count("и")+ val.count("а") == 1:
        last_pos == pos
print(pos)