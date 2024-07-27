# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'


print(pessoa[chave])

pessoa[chave] = 'Maria'

# Deletar Chave
del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome', 'Não existe')) # Se não existe retorna: 'Não existe'
if pessoa.get('sobrenome') is None: # get tenta obter uma chave, retorna NONE se não existir
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')
