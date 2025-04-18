for n in range(0,1000000):
    a = ">"+("0" * 100) + ("1" * n) + ("2" * 11)


    while ">1" in a or ">2"  in a or ">0" in a:
        a = a.replace(">1", "22>", 1)
        a = a.replace(">2", "2>", 1)
        a = a.replace(">0", "1>", 1)
    break
    print(n)
    #otmena