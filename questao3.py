""" 03 - Utilizando estruturas de repetição com teste lógico, faça um 
rama que peça uma senha para iniciar seu processamento, só deixe 
o usuário continuar se a senha estiver correta, após entrar dê 
boas vindas a seu usuário e apresente a ele o jogo da advinhação,
 onde o computador vai “pensar” em um número entre 0 e 10. 
 O jogador vai tentar adivinhar qual número foi escolhido até
 acertar, a cada palpite do usuário diga a ele se o número 
 escolhido pelo computador é maior ou menor ao que ele palpitou, 
 no final mostre quantos palpites foram necessários para vencer. """

import random

senha = input('Digite a senha de acesso com 4 números: ')

while senha != '4532':
    print('Senha inválida! Tente novamente: ')
    senha = input('Digite a senha com 4 números: ')

print('-' * 50)
print('Seja bem vindo! Você desbloqueou o jogo.')
print('Tente adivinhar o número escolhido pelo computador.')

computer = random.randint(0, 10)

jogador = int(input('Digite um número de 0 a 10: '))
cont = 1

while jogador != computer:
    if jogador > computer:
        print(f'{jogador} é maior')
    else:
        print(f'{jogador} é menor')
    print('Tente novamente.')
    jogador = int(input('Digite um número: '))
    cont +=1

print(f'Parabéns! Você acertou na {cont}ª tentativa!')

