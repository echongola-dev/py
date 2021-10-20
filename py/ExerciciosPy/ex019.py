from random import choice
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O nome escolhido foi: {}'.format(escolhido))



if escolhido in 'Edio edio chongola Chongola':
  print('<<<>>>')
  print('O Proprio Zamanai')
else:
    print('<<<>>>')
    print('O ' + escolhido +' e um impostor!')
