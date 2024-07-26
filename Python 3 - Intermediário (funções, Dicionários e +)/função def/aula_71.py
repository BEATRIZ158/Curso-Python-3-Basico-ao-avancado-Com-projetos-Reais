# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

while True:
    print("-=" * 10, " MULTIPLICADOR ", "-="*10)
    print("[ 1 ] - Adicionar Valores\n[ 2 ] - Sair")
    op = input("Sua opção? ")
    
    try:
        op = int(op)
        if op == 1:
            valores = input("Digite os valores: ").strip().split()
            try:
                valores = [float(valor) for valor in valores]
                total = multiplica(*valores)
                print(total)
            except ValueError:
                print("Todos os valores precisam ser numéricos")
        elif op == 2:
            print("Saindo ...")
            break
        else:
            print("Opção indisponível!")
    except ValueError:
        print("A opção escolhida deve ser um número inteiro!")

# Par ou Impar

def par_impar(*args):
    resultados = []
    for numero in args:
        if numero % 2 == 0:
            resultados.append(f'O número {numero} é PAR')
        else:
            resultados.append(f'O número {numero} é IMPAR')
    return resultados

while True:
    print("-=" * 10, " PAR OU IMPAR? ", "-="*10)
    print("[ 1 ] - Adicionar Valores\n[ 2 ] - Sair")
    op = input("Sua opção? ")
    
    try:
        op = int(op)
        if op == 1:
            valores = input("Digite os valores: ").strip().split()
            try:
                valores = [float(valor) for valor in valores]
                teste = par_impar(*valores)
                for resultado in teste:
                    print(resultado)
            except ValueError:
                print("Todos os valores precisam ser numéricos")
        elif op == 2:
            print("Saindo ...")
            break
        else:
            print("Opção indisponível!")
    except ValueError:
        print("A opção escolhida deve ser um número inteiro!")
