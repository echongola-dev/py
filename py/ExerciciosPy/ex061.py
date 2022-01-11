# quando usamos o for

'''primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('ACABOU')'''

# quando usamos o While
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(' {} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')