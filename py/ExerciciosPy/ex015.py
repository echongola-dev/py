dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 150)
print('O total a pagar e de {:.2f} Meticias.'.format(pago))
