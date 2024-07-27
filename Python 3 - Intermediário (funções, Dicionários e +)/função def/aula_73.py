"""
Closure e funções que retornam outras funções

A função externa criar_saudacao retorna a função saudar
quando chamamos criar_saudacao em falar_bom_dia, a mensagem 
passada é armezanda e saudar é retornada.
Quando chamamos falar_bom_dia, saudar lembra da mensagem 
passada (Nesse caso 'Bom dia') mesmo após a execução de
criar_saudacao
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

# Closure, o Python guarda o valor da função criar_saudacao

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
