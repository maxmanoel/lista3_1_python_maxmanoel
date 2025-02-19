#No Senailândia mulheres e homens podem servir o exercício do País. O serviço é opcional e é muito comum que asa pessoas se 
#apresentem para o serviço em algum momento da vida. Existe uma única restrição para o ingresso que é a idade da pessoa

nome = (input("Digite o seu nome : "))
idade = int(input("Digite o sua idade : "))
genero = (input("Digite o seu genero (F ou M): "))
if genero == 'f' or 'F' and idade == 21 and idade <= 34:
    print("Você poderá servir.")
    print("MAX MANOEL")

elif genero == 'm' or 'M' and idade == 18 and idade <= 39:
    print("Você poderá servir.")
    print("MAX MANOEL")

else:
    print("inválido.")
    print("MAX MANOEL")
