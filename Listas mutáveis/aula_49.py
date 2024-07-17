"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50) # Adiciona ao final da lista
lista.pop() # Normalmente usado para eliminar o último elemento, é um método
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)

# Ou remove
lista = ['Beatriz', 22, 1.70, 'Linda']
print(lista)
lista.remove('Linda') # Só aceita o valor do elemento, e não o índice
print(f"Removi Linda: {lista}")
