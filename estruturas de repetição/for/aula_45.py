"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
#texto = iter('Beatriz')  # __iter__()
texto = 'Beatriz'

#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())

#ou

#print(next(texto))

# print(texto.__next__())  Dá erro, não tem mais valores
iteratador = iter(texto)  # iterator

# Como o while trata esse erro
while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration: # Ao chegar no fim, ele para o laço
        break

# Como o for trata esse erro
#for letra in texto:
#    print(letra)
