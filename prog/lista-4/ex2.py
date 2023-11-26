def main():
    n = int(input())
    for j in range (n): #quantidade de vezes que vai ser executada 
        a = input()
        vet = []
        tamanho = len(a) #contabiliza tamanho da string
        

        for i in range(tamanho):
            vet.append(a[i]) #adiciona um elemento no final do vetor
            
        for i in range ((tamanho//2)-1 , -1, -1):
            print(vet[i], end="") #evita quebra de linha]
    
        for i in range (tamanho-1, (tamanho//2)-1,-1 ):
            print(vet[i], end= "")
        print()

if __name__ == "__main__":
    main()