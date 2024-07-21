""" Calculadora com while """

operadores = '+-/*'
while True:
    print(" - - - - - CALCULADORA - - - - - ")
    num_1 = input("Primeiro Valor: ").replace(',', '.')
    num_2 = input("Segundo Valor: ").replace(',', '.')
    resultado = 0
    operador = ' '
    
    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
    except ValueError:
        print("Não foi possível converter o valor!")
    
    while True: 
        operador = input("Defina um operador (+ - / *): ").lower()
        if operador not in operadores:
            print("Operador indisponível tente novamente!")
        else:
            break
    if operador == '+':
        resultado = num_1 + num_2
    elif operador == '-':
        resultado = num_1 - num_2
    elif operador == '/':
        resultado = num_1 / num_2
    else:
        resultado = num_1 * num_2
    print(" - "* 20)
    print(f"O resultado de {num_1:.2f} {operador} {num_2:.2f} = {resultado:.2f}")
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair == 's':
        print("Saindo da calculadora....")
        break

# Ou

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print("Realizando sua conta. Confira o resultado abaixo: ")
    
    if operador == '+':
        print(f"{num_1_float}+{num_2_float}=", num_1_float+num_2_float)
    elif operador == '-':
        print(f"{num_1_float}-{num_2_float}=", num_1_float-num_2_float)
    elif operador == '/':
        print(f"{num_1_float}/{num_2_float}=", num_1_float/num_2_float)
    elif operador == '*':
        print(f"{num_1_float}*{num_2_float}=", num_1_float*num_2_float)
    else:
        print('Nunca deveria chegar aqui.')
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
