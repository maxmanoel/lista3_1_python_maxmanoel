#02 - Escreva um programa para exibir na tela o nome e a categoria, o programa deve ler o String para o nome e um 
#número real para o peso. Conforme o peso ocorrerá o enquadramento na categoria



nome = (str("Digite seu nome : "))
peso = int(input("Digite seu peso : "))
if peso < 52:
    print('Você não esta em um peso adequado para alguma categoria.')
    print("MAX MANOEL")
elif peso >= 52 and peso < 85:
    print('Você esta na categoria peso Pena')
    print("MAX MANOEL")
elif peso >= 65 and peso <72:
    print('Você esta na categoria peso Leve')
    print("MAX MANOEL")
elif peso >=72 and peso <79:
    print('Você esta na categoria peso Ligeiro')
    print("MAX MANOEL")
elif peso >=79 and peso <86:
    print('Você esta na categoria peso Meio-Médio')
    print("MAX MANOEL")
elif peso >= 86 and peso <90:
    print('Você esta na categoria peso Médio')
    print("MAX MANOEL")
elif peso >=90 and peso <100:
    print('Você esta na categoria peso Meio-Pesado')
    print("MAX MANOEL")
elif peso >=100:
    print('Você esta na categoria peso Pesado')
    print("MAX MANOEL")