def main (): #funcao principal
    termo
    3= int(input())
    qtd = int(input())
    prod = funMult(termo, qtd)
    print (prod)

def funMult(t, quant):
    if isinstance (t, int) and isinstance (quant, int ) and quant > 0:
        if quant == 1:
            return (t)
        else:
            return t + funMult( t, quant - 1) 

if __name__ == "__main__":
    main()