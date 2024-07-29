# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz') itera sobre o valor
#s1 = set()  # vazio, tudo que fica azul é Classe
#print(s1) 
#s1 = {'Luiz', 1, 2, 3}  # com dados
#print(s1)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
s1 = {1, 2, 3, 3, 3, 3, 3, 1}
print(s1)

# - não tem índexes;

s1 = {1, 2, 3}
print(s1)

# - não garantem ordem;
s1 = set('Luiz')
print(s1)

# - são iteráveis (for, in, not in)
s1 = {1, 2, 3}
print(3 in s1)

# Convertendo
l1 = [1,2,3,3,3,3,3,1] # Crio uma lista, l1
s1 = set(l1) # Converto essa lista para set
l2 = list(s1) # Crio uma lista, l2, e recebo s1 convertido
print(l2) # Limpa valores duplicados

# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Luiz')
s1.add(1) # Só aceita 1 valor
s1.update('Olá Mundo')
s1.update(('Olá Mundo', 1, 2, 3, 4)) # Passar um iteravel
#s1.clear() #Limpando set
s1.discard('Luiz')
print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # União
s3 = s1 & s2 # Intersection, somente números que estão em ambos
s3 = s1 - s2 # Diferença, itens que está presente apenas no set da esquerda
s3 = s1 ^ s2 # Simétrica, itens que não estão em ambos, apenas em um
print(s3)
