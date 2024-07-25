"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3) # Argumentos não nomeados
soma(1, y=2, z=5) # Argumento nomeado, precisa nomear todos que vem depois do primeiro nomeado

print(1, 2, 3, sep='-')

def imprimir(a):
    print(f'{a=}') # Retorna a=1, mostra o parametro e o argumento


imprimir(1)
