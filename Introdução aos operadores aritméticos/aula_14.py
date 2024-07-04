# Formatação de strings com o método format
# Todas as variáveis em Python são objetos, porque pode fazer ações (métodos)
a = 'AAAA'
b = 'BBBB'
c = 1.1
string = 'a={nome1},b={nome2},c={nome3:.2f}' # Não dependo da ordem, passo o indice do valor
formato = string.format(
    nome1 = a, nome2 = b, nome3 = c) #a,b,c são argumentos da função format

print(formato)

# Parâmetro nomeado, quando dou um nome para os argumentos nas funções
