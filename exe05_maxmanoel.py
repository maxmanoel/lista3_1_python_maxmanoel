#05 - No comércio o conceito de margem bruta é uma 5 que é aplicada ao preço de custo para se obter o preço de venda. 
#Uma loja tem como política comercial, aplicar uma margem bruta de 45% quando o preço bruto é <= 100 kwanzas 
#e o produto custa > 100 a margem bruta é de 35% . Escreva um programa que leia o preço  do produto e mostre o seu custo.

preco_custo=float(input("Qual o preço de custo do produto: "))
if preco_custo >=100:
    preco_final=(preco_custo*0.35)+preco_custo
else:
    preco_final=(preco_custo*0.45)+preco_custo
print("A margem bruta é de: ",preco_final)
print("")
print("MAX MANOEL")