from ipaddress import ip_network,ip_address
net=ip_network('102.141.0.0/255.255.192.0.',False)
cnt=0
for i in net:
    i=f'{int(i):032b}'
    if  i.count('1')%7==0:
        cnt+=1
        print(cnt)

