from itertools import product
alph=("школа")
alph= sorted(alph)
for pos,val in enumerate(product(alph, repeat=5),start=1):
    val = "".join(val)
    if ("шалаш") in val:
        last_pos=pos
print(last_pos)
