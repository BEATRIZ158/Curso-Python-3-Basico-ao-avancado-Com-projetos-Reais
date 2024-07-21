"""
Tipo tupla - Uma lista imutável
"""
nomes = ('Maria', 'Helena', 'Luiz')
# nomes = tuple(nomes) Converter Lista para Tupla
# nomes = list(nomes) Converter Tupla para Lista
print(nomes[-1])
print(nomes)

"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)
print(next(lista_enumerada))

#for indice, nome in enumerate(lista):
#    print(indice, nome, lista[indice])

#for item in enumerate(lista):
#    indice, nome = item  #indice recebe 0, nome recebe 'Maria'
#    print(indice, nome)

#for tupla_enumerada in enumerate(lista):
#    print('FOR da tupla:')
#    for valor in tupla_enumerada:
#        print(f'\t{valor}')
