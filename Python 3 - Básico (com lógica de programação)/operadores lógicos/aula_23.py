# Operador lógico "input
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if senha != '123456':
    print("Senha incorreta.")

# string vasia é False
if not senha:
    print("Você não digitou nada")

print(not True)
print(not 0) # True, o inverso de False
print(not 1) # False, o inverso de True
