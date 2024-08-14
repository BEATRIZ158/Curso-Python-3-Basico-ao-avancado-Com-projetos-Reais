lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
lista = [
    (x, y) # Isso é o que vai ser incluído na lista pelo for
    for x in range(3)
    for y in range(3)
]
lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista)
