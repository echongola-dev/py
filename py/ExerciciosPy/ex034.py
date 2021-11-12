sal = float(input('Qual e o salario do funcionario? '))
if sal <= 13750:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print('Quem ganhava {:.2f} meticais agora passa a receber {:.2f}.'.format(sal, novo))

