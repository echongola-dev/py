preco = float(input('Qual e o preco do produto? '))
novop = preco - (preco * 5 / 100)
print('o preco que custava {} meticais, na promocao com disconto de 5% vai custar {} meticais'.format(preco, novop))