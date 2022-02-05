resp = 'S'
media = soma = quant = maior = menor = 0
while resp in 'Ss':
    nume = int(input('Digite um numero: '))
    soma += nume
    quant += 1
    if quant == 1:
        maior = menor = nume
    else:
        if nume > maior:
            maior = nume
        if nume < menor:
            menor = nume
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} numeros e a Media foi {}.'.format(quant, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
