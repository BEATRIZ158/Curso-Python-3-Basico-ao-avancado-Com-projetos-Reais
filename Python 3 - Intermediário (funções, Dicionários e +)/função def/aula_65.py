"""
Introdução ás funções (def) em Python
Funções são trechos de códigod usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico
Por padrão, funções Python retornam None (nada)
"""

#def Print(a, b, c):
#    print("Várias1")
#    print("Várias2")
#    print("Várias3")
#    print("Várias4")
#    print("Várias5")

#Print() # Chama a função

def imprimir(a, b, c): # a, b, c são Parãmetros, nome da "variável" dentro dos parênteses
    print(f"Valor a: {a}")
    print(f"Valor b: {b}")
    print(f"Valor c: {c}")


imprimir(1, 2, 3) # Valores passados são argumentos
imprimir(4, 5, 6)

def saudacao(nome):
    print(f"Olá, {nome}")

saudacao('Beatriz')
saudacao('Luiz')
saudacao('Helena')
saudacao('Otávio')
