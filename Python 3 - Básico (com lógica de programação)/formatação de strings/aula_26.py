""" 
Formatação básica de strings
s - String
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{variavel:$<10}.')
print(f'{10000.12412413514193758315:,.2f}')
print(f'{10000.12412413514193758315:+,.2f}')
print(f'O hexdecimal de {1500:08X}')
print(f'{variavel!r}')
