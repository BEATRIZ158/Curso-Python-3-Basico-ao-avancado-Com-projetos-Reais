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
