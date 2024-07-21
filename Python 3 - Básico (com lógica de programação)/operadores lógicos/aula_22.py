# Operadores lógicos
# and (e) or (ou) not(not)
# or - Qualquer condição verdadeira avalia
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor
# são considerados falsy (que vc já viu)
# 0 0 .0 '' False
# Também existe o tipo none que é 
# usado para representar um não valor

# Operador or

#entrada = input('[E]ntrar [S]air')
#senha_digitada = input('Senha: ')

#senha_permitida = '123456'
#if entrada == 'E' and senha_digitada == senha_permitida:
#    print("Entrar")
#else:
#    print("Sair")

# Avaliação de curto circuito
senha = 0 or False or 0 or 'abc' or True
senha = input('Senha: ') or 'Sem sanha'
print(True or False or True)
