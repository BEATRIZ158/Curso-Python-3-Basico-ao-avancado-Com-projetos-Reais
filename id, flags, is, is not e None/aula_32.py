"""
Exe 1:
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

num = input("Digite um número inteiro: ")

try:
    # Tenta converter a entrada para um número inteiro
    num_int = int(num)
    print(f"O número {num} é inteiro!")
    if num_int % 2 == 0:
        print(f"O número {num_int} é PAR")
    else:
        print(f"O número {num_int} é IMPAR")
except ValueError:
    try:
        # Tenta converter a entrada para um número flutuante
        num_float = float(num)
        print(f"O número {num} não é um número inteiro")
    except ValueError:
        print(f"{num} não é um valor numérico")

"""

"""
Exe 2:
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

hora = input("Qual é a hora atual: ")

try:
    hora = int(hora)
    if 0 <= hora <= 11:
        print("Bom dia")
    elif 12 <= hora <= 17:
        print("Boa tarde")
    elif 18 <= hora <= 23:
        print("Boa noite")
    else:
        print("Valores negativos não são permitidos")
except ValueError:
    print("Não é horário")


"""

"""
Exe 3:
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
