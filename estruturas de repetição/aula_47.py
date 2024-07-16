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
    
    if letra in palavra_chave:
        for i, letra_chave in enumerate(palavra_chave):
            if letra_chave == letra:
                palavra_formatada[i] = letra
                cont += 1
            palavra_formatada_str = ''.join(palavra_formatada) 
            if palavra_chave == palavra_formatada_str:
                print(f"Você venceu com {cont} tentativas")
                break
    else:
        cont += 1
    print(f"Palavra formatada: {palavra_formatada_str}")

# Método join é usado para concatenar ou juntar os elementos de uma lista (ou qualquer iterável) em uma única string. 
# Ele é particularmente útil quando você tem uma lista de strings e deseja combiná-las em uma string única
