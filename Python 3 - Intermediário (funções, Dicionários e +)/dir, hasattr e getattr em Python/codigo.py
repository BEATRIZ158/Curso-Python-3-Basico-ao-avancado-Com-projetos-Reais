# As funções dir, hasattr e getattr em python são usados para interagir 
# com os atributos e métodos de forma dinâmica

#dir() retorna uma lista de todos os atributos e métodos disponíveis para um objeto
string = 'Beatriz'
metodo = 'upper'

print(dir(string)) # Mostra todos os atributos e métodos do objeto 'string'

#hasattr verifica se um objeto tem um atributo específico
#retorna True se existe e False se não existe
#Nome do método vem como string

if hasattr(string, metodo):
    print("Existe upper")
    #print(string.upper())
    #print(getattr(string, metodo))
    print(string)
else:
    print('Não existe o método', metodo)

#getattr pegar o atributo

pessoa = "Beatriz"
print(hasattr(pessoa, "upper"))     # Output: True, pois strings têm o método `upper`
print(getattr(pessoa, "upper")())   # Output: BEATRIZ, chama o método `upper` para transformar em maiúsculas
