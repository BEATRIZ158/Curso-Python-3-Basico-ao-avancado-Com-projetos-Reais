nome =  input('Qual o seu nome? ')
print(f"O seu nome é {nome=}") # Para ver o valor da variável

nome = str(input("Qual é o seu nome? "))
print(f"Seu nome é {nome}")

numero_1 = input("Digite um número: ")
numero_2 = input("Digite outro número: ")
print(f"A soma dos dois números é {numero_1 + numero_2}") # É tratado como String (str)

int_numero_1 = int(numero_1) # ùtil para checar o valor original passado
int_numero_2 = int(numero_2)

print(f"A soma dos dois números é {int_numero_1 + int_numero_2}")

#ou

numero_1 = int(input("Digite um número: ")) # Converte para inteiro
numero_2 = int(input("Digite outro número: "))

print(f"A soma dos dois números é {numero_1 + numero_2}")
