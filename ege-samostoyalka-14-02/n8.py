from itertools import product
alph=("марксл")
alph= sorted(alph)
for pos,val in enumerate(product(alph, repeat=6),start=1):
    val="".join(val)
    if 'кс' and "ск" 