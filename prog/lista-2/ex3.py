#Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.
v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())
v6 = float(input())

cont = 0

if v1 > 0: 
    cont = cont+1
if v2 > 0:
    cont = cont+1
if v3 > 0:
    cont = cont+1
if v4 > 0:
    cont = cont+1
if v5 > 0:
    cont = cont+1
if v6 > 0:
    cont = cont+1
print( cont, "valor(es) postivo(s)")