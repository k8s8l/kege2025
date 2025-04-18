with open('17_19249.txt'    ) as file:
        data=[int(i) for i in file]
max_43 = max(i for i in data if str(i)[-2:] =='43')
ans=[]
for i in range(len(data)-2):
    num1,num2,num3 =data [i:i+3]
    summ= num1+num2+num3
    u1 = len(str(num1)) ==4
    u2 = len(str(num2)) ==4
    u3 = len(str(num3)) ==4
    f1=u1+u2+u3==1
    f2= summ >=max_43
    if f1 and f2:
        ans.append(summ)

print(len(ans)), max(ans)

