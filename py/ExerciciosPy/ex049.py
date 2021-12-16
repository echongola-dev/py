numero = int(input('Digite o numero pra ver a sua tabuada: '))
for c in range(1, 11):  
    print('{} x {:2} = {}'.format(numero, c, numero*c))
