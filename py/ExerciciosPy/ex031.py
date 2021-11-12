Distancia = float(input('Qual e a distancia da viagem? '))
print('Voce esta prestes a comecar uma viagem de {}Km'.format(Distancia))

'''if Distancia <= 200:
    preco = Distancia * 2
else:
    preco = Distancia * 10'''

preco = Distancia * 2 if Distancia <= 200 else Distancia * 10
print('E o preco da sua viagem sera de {:.2f} meticais.'.format(preco))
