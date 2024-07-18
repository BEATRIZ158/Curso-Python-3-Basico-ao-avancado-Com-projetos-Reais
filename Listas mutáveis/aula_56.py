"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')

""" 
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permite que o programa quebre com
erros de índices inexistentes na lista
"""
lista = []

while True:
    print("=-="*20)
    op = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar [s]air:").lower().split()[0]

    try:
        op = int(op)
        print("A opção escolhida deve ser uma letra. Tente novamente!")
    except ValueError:
        try:
            op = float(op)
            print("A opção escolhida deve ser uma letra. Tente novamente!")
        except ValueError:
            op = str(op)
            if op == 'i':
                valor = input('Valor: ')
                lista.append(valor)
                print(f"Lista {valor} foi criada")
            elif op == 'a':
                while True:
                    indice = input("Digite o índice: ")
                    try:
                        indice = int(indice)
                        if 0 <= indice < len(lista):
                            print(f"A lista {lista[indice]} foi apagada com sucesso!")
                            del lista[indice]
                            break
                        else:
                            print("Índice indisponível. Tente novamente!")
                    except ValueError:
                        print("Erro! Precisa ser um índice INTEIRO! Tente novamente.")
            elif op == 'l':
                print("Você escolheu Listar!")
                for indice, valor in enumerate(lista):
                    print(indice, valor)
            elif op == 's':
                print("Você escolheu sair! Tchau, tchau...")
                break
            else:
                print("Opçõa errada!")
