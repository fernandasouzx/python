valores = input().split()
v1, v2, v3, v4 = float(valores[0]), float(valores[1]), float(valores[2]), float(valores[3])
try:
    nota_exame = input()
except:
    nota_exame = ""

media = ((v1*2)+ (v2*3) + (v3*4) + (v4*1))/10
print("Media: %.1f"%media)

if media >= 7.0:
    print("Aluno aprovado.")
elif media >=5.0 and media <=6.9:
    print("Aluno em exame.")
else:
    print("Aluno reprovado.")

if (nota_exame != ""):
    nota_exame = float(nota_exame)
    print("Nota do exame:", nota_exame)

    media2 = (nota_exame + media)/2

    if media2 >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    media_final = media2
    print("Media final:", media2)