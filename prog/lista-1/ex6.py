# A = float(input())
# B = float(input())
# C = float(input())
# triang = A*C/2
# circ = 3,14159*C**2
# trap = ((A+B)*C)/2
# print(trap)

valores = input().split()
a, b, c = float(valores[0]), float(valores[1]), float(valores[2])
triang = (a*c)/2
circ = 3.14159*c**2
trap = (a+b)*c/2
quadrado = b*b
retangulo = a*b
print("TRIANGULO: %.3f"%triang)
print("CIRCULO: %.3f"%circ)
print("TRAPÉZIO: %.3f"%trap)
print("QUADRADO: %.3f"%quadrado)
print("RETANGULO: %.3f"%retangulo)

