"""
Iterando strings com while
"""
#       012345678910
nome = 'Beatriz'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

# Solução do exercício

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += letra
    indice += 1
    
print(novo_nome)
