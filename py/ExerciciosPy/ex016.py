'''import math
num = float(input('Digite um numero: '))
print('O valor digitado foi {} e a sua porcao inteira e {}'.format(num, math.trunc(num)))'''


# As duas formas funcionam!


num = float(input('Digite um numero: '))
print('O valor digitado foi {} e a sua porcao inteira e {}.'.format(num, int(num)))