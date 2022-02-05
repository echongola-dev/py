nu = cont = soma = 0
nu = int(input('Digite um numero [999 paara parar]: '))
while nu != 999:
    soma += nu
    cont += 1 
    nu = int(input('Digite um numero [999 paara parar]: '))
print('Voce digitou {} numeros e a soma entre eles foi {}.'.format(cont, soma))