from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:36][::-1]:
    num1 = int(f'51{x}29', 36)
    num2 = int(f'{x}023', 36)
    res = num1 + num2
    if res % 149 == 0:
        print(res // 149)
        break
        #насущний вопрос почему
