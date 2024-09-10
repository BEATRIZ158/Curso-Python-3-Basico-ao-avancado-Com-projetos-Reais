# Dictionary Comprehension e Set Comprehension
# São maneiras concisas de criar dicionários e conjuntos
# a partir de iteráveis, usando sintaxe semelhante à das
# List Comphehensions

# Forma padrão de criar um dicionário
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# Usando Dic Comprehension para criar um Dicionário
# isinstance(valor, str): Retorna True se valor for uma instância
# da classe str, caso contrário, retorna False

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

# Primeiro temos uma forma padrão de criar uma lista
lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]

# Criando um dicionário a partir da lista de tuplas
dc = {
    chave: valor
    for chave, valor in lista
}

# Criando um conjunto (set) usando Set Comprehension
s1 = {2 ** i for i in range(10)}
print(s1)
