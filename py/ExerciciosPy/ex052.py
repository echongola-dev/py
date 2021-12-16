inteiro = int(input('Digite um numero: '))
tot = 0
for c in range(1, inteiro + 1):
    if inteiro % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel por {} vezes'.format(inteiro, tot))
if tot == 2:
    print('Por isso ele e PRIMO')
elif tot == 0:
    print('Por isso ele NAO E PRIMO')