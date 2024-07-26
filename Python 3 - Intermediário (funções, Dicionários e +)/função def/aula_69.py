"""
Retorno de valores das funções (return)
"""

def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y # Não será executado se o if for True


# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2) # Função soma sem return só projeta o resultado na tela, não retorna
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))
