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
import random

palavra_secreta = ['python', 'programação', 'ciência', 'jogos', 'faculdade', 'estudos']
palavra_aleatoria = random.choice(palavra_secreta)

tamanho_palavra = len(palavra_aleatoria)
palavra_corrente = ['*'] * tamanho_palavra

print("O tamanho da palavra é {}".format(tamanho_palavra))

acertos = 0;

while(True):
    letra = input("Digite uma letra: ").lower()

    try: 
        if len(letra) > 1:
            print("Digite apenas uma letra!")
            continue  

        for i in range(tamanho_palavra): 
            if palavra_aleatoria[i] == letra:
                palavra_corrente[i] = letra
                acertos += 1
        print(palavra_corrente)

        if acertos == len(palavra_aleatoria):
            print("\n")
            print("Parabéns! Você acertou, a palavra secreta era '{}'".format(palavra_aleatoria))
            print("\n")

    except:
        print("erro")

       
        
