"""
Introdução ao empacotamento e desempacotamento
"""
#nomes = ['Maria', 'Helena', 'Luiz']
#nome1, nome2, nome3 = nomes
#print(nome2)

nome, *resto = ['Maria', 'Helena', 'Luiz'] # Pegar somente um valor
print(nome, resto)

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz'] # Pegar somente um valor
print(nome, resto) # Indica que as variáveis está ali, mas não vão ser usadas

_, nome2, *_ = ['Maria', 'Helena', 'Luiz']
print(nome2)
