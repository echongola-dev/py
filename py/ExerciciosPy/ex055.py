maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}a pessoa: '.format(p)))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O Maior peso lido foi de {}Kg.'.format(maior))
print('O Menor peso lido foi de {}Kg.'.format(menor))
