"""
for in com listas
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']

for ind, nome in enumerate(lista):
    print(f"O índice {ind} tem o nome {nome}")

# Ou

indices = range(len(lista))

for indice in indices:
    print(f"O índice {indice} tem o nome {lista[indice]}")
