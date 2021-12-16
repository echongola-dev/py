soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 ==  0:
        cont += 1 # O '+=' significa que adiciona ele mesmo mais o valor que vier a seguir.
        soma += c
        print(c, end=' ')
print('A soma de todos os {} valores solicitados e {}.'.format(cont, soma))
    