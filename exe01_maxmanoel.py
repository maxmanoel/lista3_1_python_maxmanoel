#01 - Escreva um programa que forneça um tipo de aplicação financeira adequada a um investidor a partir de 2 dados fornecidos: 
# O grau de aceitação de risco e o valor a ser investido. O grau de aceitação de risco deve ser lido no teclado na forma
#de BX(baixo risco) ou AL(alto risco) se for fornecido algo diferente disto o programa deve mostrar uma mensagem indicando
#que foi fornecido dado inválido. Para o valor ser deve ser um número real.

grau = input("Digite o grau de risco que você quer: ")
valor = int(input("Digite o valor à ser investido: "))
if grau == 'BX' and valor < 1000:
    print('Coloque na poupança')
    print("MAX MANOEL")

elif grau == 'BX' and valor >= 1000:
    print('Coloque na Renda Fixa')
    print("MAX MANOEL")

elif grau == 'AL' and valor < 1000:
    print('Coloque em bitcoins')
    print("MAX MANOEL")

elif grau == 'AL' and valor >= 1000:
    print('Coloque em ações')
    print("MAX MANOEL")

else:
    print('dado inválido')
    print("MAX MANOEL")

 