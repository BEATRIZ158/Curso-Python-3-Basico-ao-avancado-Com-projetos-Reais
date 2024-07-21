# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
# O t á v i o
# -6-5-4-3-2-1

nome = 'Beatriz'

# [1] Indices
print(nome[0]) # B
print(nome[1]) # e
print(nome[2]) # a
print(nome[3]) # t
print(nome[4]) # r
print(nome[5]) # i
print(nome[6]) # z

print('-'*10)
# ou - De trá para frente

print(nome[-7]) # B
print(nome[-6]) # e
print(nome[-5]) # a
print(nome[-4]) # t
print(nome[-3]) # r
print(nome[-2]) # i
print(nome[-1]) # z

print('-'*10)

print('a' in nome) # True
print('s' not in nome) # True
print('B' not in nome) # False

print('-'*10)

nome = input("Digite um nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")
