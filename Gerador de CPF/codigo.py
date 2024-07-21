"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  5   1  9  1  7  8  4  1  8
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
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
                
            try:
                cpf_numeros = [int(numero) for numero in cpf]
            except ValueError:
                print("CPF deve conter apenas números.")
                cpf_numeros = []
            if cpf_numeros:
                resultados = []
                cont = 0
                for num in range(10, 1, -1):  # Corrigi a range para 1
                    resultados.append(cpf_numeros[cont] * num)
                    cont += 1
                print(f"Resultados: {resultados}")
                
                resultado = (sum(resultados) * 10) % 11
                if resultado > 9:
                    resultado = 0
                else:
                    resultado = resultado
                print(f"Resultado do primeiro digito é {resultado}")
                
        elif op == 2:
            print("Você escolheu sair. Tchau, tchau...")
            break
        else:
            print("Opção indisponível. Tente novamente!")

    except ValueError:
        print("A opção escolhida precisa ser um número INTEIRO! Tente novamente.")
