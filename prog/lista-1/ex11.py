segundos= int(input())
hora = segundos//3600
segundos = segundos % 3600
minutos = segundos//60
segundos = segundos % 60



print(str(hora)+":"+str(minutos)+":"+str(segundos))