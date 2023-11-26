X = []
for i in range(10):
    valor = int(input())
    if valor <= 0:
        valor = 1
        X.insert(i,valor)
    else:
        X.insert(i,valor)

for i in range(10):
    print('X[{0}] = {1}'.format(i,X[i]))