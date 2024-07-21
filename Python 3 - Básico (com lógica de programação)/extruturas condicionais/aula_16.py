#Introdução aos blocos de código + if / elif / else

# if / elif        / else
# se / se não se   / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print("Voce entrou no sistema!") # Indentação
elif entrada == 'sair': # Senão entrou na primeira, tenho outra opção
    print("Você saiu do sistema")
else:
    print("Você digitou uma opção inválida") # Depende do if

print("FORA DOS BLOCOS")
