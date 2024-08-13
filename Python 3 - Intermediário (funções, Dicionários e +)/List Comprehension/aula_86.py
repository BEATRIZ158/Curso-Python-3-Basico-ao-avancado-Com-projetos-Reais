# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2 # Deste lado (Esquerdo) fica o valor que será incluído na lista
    for numero in range(10) # Gera os valores
]
print(lista)
