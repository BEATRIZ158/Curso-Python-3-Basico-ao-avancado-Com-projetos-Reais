# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True) # Muda a ordem (inverte)
# sorted(lista)
lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def ordena(item):
    return item['sobrenome']

lista.sort(key=ordena) # ordena retorna item[sobrenome] sort ordena pelo sobrenome
print(lista)

def exibir(lista):
    for item in lista:
        print(item)
    print()

# Passa uma função em key=
l1 = sorted(lista, key=lambda item: item['nome']) # Primeiro parametro é a lista, segundo é o item
l2 = sorted(lista, key=lambda item: item['sobrenome']) # Sorte retorna uma cópia rasa

exibir(l1)
exibir(l2)
