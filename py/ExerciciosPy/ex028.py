from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador sorteiar
print('-=-' * 20)
print('Vou sorteiar um numero entre 0 e 5. Tente Advinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei?  ')) # Jogador tenta advinhar
print('Processando...')
sleep(5)
if jogador == computador:
    print('Parabens! Voce coseguiu me vencer!')
else: 
    print('Ganhei! Eu pensei no numero {} e nao no {}!'.format(computador, jogador))
