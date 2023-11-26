#Faça um programa que leia o nome do vendedor, seu salário fixo e o total das vendas realizadas por ele no mês (em dinheiro). Considerando que este vendedor recebe 15% sobre todos os produtos vendidos, escreva o salário final (total) deste vendedor no final do mês, com duas casas decimais.

vendendor = input()
salario = float(input())
total_vendas =  float(input())
comissao = total_vendas*0.15
total= comissao + salario
print("TOTAL = R$ %.2f"%total)