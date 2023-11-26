valores1 = input().split()
valores2 = input().split()
x1, y1, x2, y2 = float(valores1[0]), float(valores1[1]), float(valores2[0]), float(valores2[1])

distancia = ((x2-x1)**2+(y2-y1)**2)**0.5

print("%.4f"%distancia)
