"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
while True:
    print("""{} GERADOR DE CPF {}
[ 1 ] - Gerar CPF
[ 2 ] - Sair
""".format('*'*10, '*'*10))
    
    op = input("Sua opção?(1 ou 2)  ").replace(' ', '')
    
    try:
        op = int(op)
        
        if op == 1:
            while True:
                valores = input("Digite seu CPF: ")
                cpf = list(valores)
            
                if len(cpf) != 9:
                    print("Você precisa passar 9 dígitos! Tente novamente.")
                else:
                    break
            # Descobirndo o primeiro digito!
            try:
                cpf_numeros = [int(numero) for numero in cpf]
            except ValueError:
                print("CPF deve conter apenas números.")
                cpf_numeros = []
            while len(cpf_numeros) != 11:
                if cpf_numeros:
                    resultados = []
                    cont = 0
                    inicio = 10 if len(cpf_numeros) == 9 else 11
                    for num in range(inicio, 1, -1):
                        resultados.append(cpf_numeros[cont] * num)
                        cont += 1
                    resultado = (sum(resultados) * 10) % 11
                    if resultado > 9:
                        resultado = 0
                    else:
                        resultado = resultado
                    cpf_numeros.append(resultado)    
            print("CPF completo: ", end='')
            for digito in cpf_numeros:
                print(digito, end=' ')
            print()
        elif op == 2:
            print("Você escolheu sair. Tchau, tchau...")
            break
        else:
            print("Opção indisponível. Tente novamente!")

    except ValueError:
        print("A opção escolhida precisa ser um número INTEIRO! Tente novamente.")
