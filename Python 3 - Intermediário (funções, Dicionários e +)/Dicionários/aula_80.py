# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

while True:
    print("-="*20)
    print("""SISTEMA DE PERGUNTAS E RESPOSTAS
[ 1 ] - Iniciar Perguntas
[ 2 ] - Sair do Sistema
""")
    op = input("Sua opção(1 ou 2): ")
    
    try:
        op = int(op)
        if op == 1:
            certas = 0
            for pergunta in perguntas:
                print(f"Pergunta: {pergunta['Pergunta']}")
                for i, opcao in enumerate(pergunta['Opções']):
                    print(f"{i + 1}. {opcao}")
                while True:
                    resposta = input("Sua resposta: ")
                    try:
                        resposta = int(resposta) - 1
                        if resposta < 0 or resposta >= len(pergunta['Opções']):
                            print("Opção inválida. Tente novamente.")
                            continue
                        else:
                            break
                    except ValueError:
                        print("A resposta precisa estar entre 1 e 4. Tente novamente!")
                resposta_usuario = pergunta['Opções'][resposta]
                if resposta_usuario == pergunta['Resposta']:
                    print("Acertou 👍")
                    certas += 1
                else:
                    print("Errou ❌")
            print(f"Você acertou {certas} de 3 perguntas")
        elif op == 2:
            print("Saindo...")
            break
        else:
            print("Valor indisponível. Tente novamente!")
    except ValueError:
        print("A opção escolhida deve ser 1 ou 2!")

# Professor

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
