from itertools import product
count = 0
for num in product('0123456789ab', repeat=7:
    if num.count('b') == 2 and num[0] !='0':
        x = ''.join(num)
        x = x.replace('2','4').replace('2','6').replace('2','8').replace('4','6').replace('4','4').replace('4','8').replace('4','8')
        if x.count('86') == 0 and x.count('68') == 0:
            count+=1
print(count)
#не решено
