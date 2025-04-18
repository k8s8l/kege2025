from itertools import product
alph= sorted("ясновидец")
sogl='снвдц'
ans=[]
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val=''.join(val)
    if pos%2!=0 and val[-1] in 'снвдц':
        if
