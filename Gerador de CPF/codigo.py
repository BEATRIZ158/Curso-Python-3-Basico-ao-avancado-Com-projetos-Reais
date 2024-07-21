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
                    try:
                        cpf_numeros = [int(numero) for numero in cpf]
                        break
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
                    resultado = 0 if resultado > 9 else resultado
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

"""Solução do Professor

# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
import re
import sys

# cpf_enviado_usuario = '746.824.890-70' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')
entrada = input('CPF [746.824.890-70]: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')
"""