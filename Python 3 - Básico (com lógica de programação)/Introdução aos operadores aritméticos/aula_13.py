# Formatação de strings
# fString
nome = 'Beatriz'
altura = 1.80
peso = 95
imc = peso / altura ** 2

# :.2f  trata as casas decimais
linha_1 = f"{nome} tem {altura:.2f} de altura"
linha_2 = f"pesa {peso} quilos e seu imc é"
linha_3 = f"{imc:.2f}"

print(linha_1)
print(linha_2)
print(linha_3)
