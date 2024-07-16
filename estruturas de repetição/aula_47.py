"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_chave = 'abacate'
cont = 0
palavra_formatada = list('*******')

while True:
    letra = input("Digite uma letra: ").lower()[0]
    cont += 1
    
    if letra in palavra_chave:
        for i, letra_chave in enumerate(palavra_chave):
            if letra_chave == letra:
                palavra_formatada[i] = letra
            palavra_formatada_str = ''.join(palavra_formatada) 
            if palavra_chave == palavra_formatada_str:
                print(f"Você venceu!")
                print(f"A palavra era {palavra_chave}")
                print(f"Tentativas: {cont} ")
                break
    print(f"Palavra formatada: {palavra_formatada_str}")

# Método join é usado para concatenar ou juntar os elementos de uma lista (ou qualquer iterável) em uma única string. 
# Ele é particularmente útil quando você tem uma lista de strings e deseja combiná-las em uma string única
#ou

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
