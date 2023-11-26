y = float(input())
z = []
for i in range(100):
    if i == 0:
        auy = y
        z.insert(i,auy)
    else:
        auy = auy / 2
        z.insert(i,auy)    
for i in range(100):
    print('N[{0}] = {1:.4f}'.format(i,z[i]))