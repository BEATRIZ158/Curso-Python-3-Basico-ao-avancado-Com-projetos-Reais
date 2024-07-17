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
