# Uma empresa financeira concede empréstimos a pessoas física quando o valor da parcela é menor que 8% do salário da pessoa.
#Escreva um programa que leia 2 números reais. Valor do salário  e o valor da parcela e se o empréstimo será concedido ou não.


salario = int(input("Digite o seu salário : "))
parcela = int(input("Digite quantas vezes você irá parcelar : "))
porcentagem = (8/100) * 100
if parcela < porcentagem:
    print("Empréstimo condedido.")
    print("MAX MANOEL")
else:
    print("Empréstimo não concedido.")
    print("MAX MANOEL")