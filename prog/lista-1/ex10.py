valor = int(input())
notas = [100,50,20,10,5,2,1]
print (valor)
for x in notas:
    print ("%i nota(s) de R$ %d,00"%((valor/x),x))
    valor %= (x)