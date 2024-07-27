# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# def duplicar(numero):
#     return numero * 2


# def triplicar(numero):
#     return numero * 3


# def quadruplicar(numero):
#     return numero * 4
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2) # Salva o valor 2 em duplicar()
triplicar = criar_multiplicador(3) # Salva o valor 3 em triplicar()
quadruplicar = criar_multiplicador(4) # Salva o valor 4 em quadruplicar()

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
