""" 
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade
de caracteres da string (str)
"""
variavel = 'Olá mundo'
print(variavel[4:]) # mundo, Vai até o fim 
print(variavel[4:9]) # mundo, Vai até o fim 
print(variavel[0:5]) # Olá m, do 0 ao 4 
print(variavel[-8:-2]) # lá mun, do 0 ao 5
print(len(variavel[3])) # 1
print(len(variavel)) # 9, retorna o tamanho
print(variavel[0:9:2]) # 0 Inicio, f Fim, p Passo
print(variavel[::-1]) # Inverte
print(variavel[-1:-10:-1]) # Inverte, do -1 ao -10 de 1 em 1
