salario = float(input('Qual e o salario do funcionario? '))
per = (salario * 15 / 100)
novo = salario + per
print('Um funcionario que ganhava {:.2f} meticais, com aumento de 15% que sao {}, passa a receber {:.2f} meticais'.format(salario, per, novo))