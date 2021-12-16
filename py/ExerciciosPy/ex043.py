peso = float(input('Qual e o seu peso? (kg) '))
alt = float(input('Qual e a sua altura? (m) '))
imc = peso / (alt ** 2)
print('O IMC dessa pessoa e de {:.1f}'.format(imc), end='')
if imc < 18.5:
    print(' e esta ABAIXO DO PESO NORMAL.')
elif 18.5 <= imc <= 25:
    print('esta no PESO IDEAL.')
elif 25 <= imc <= 30:
    print('e esta no SOBREPESO')
elif 30 <= imc <= 40:
    print('e esta na OBESIDADE.')
else:
    print(' e esta na OBESIDADE MORBIDA.')
