# Compra de uma casa usando o salario mensal do trabalhador

casa = float(input('Valor da casa em meticais: '))
salario = float(input('O valor do salario em meticais: '))
anosPagamentos = float(input('Em quanto quantos anos pretende pagar a casa: '))
prestacao = casa / (anosPagamentos * 12)
minimo = salario * (30 / 100)
print('Para pagar uma casa de {:.2f} meticias em {} anos '.format(casa, anosPagamentos), end='')
print('a prestacao sera de {:.2f} meticias'.format(prestacao))
if prestacao <= minimo:
    print('O empresto e CREDITADO')
else:
    print('Emprestimo NEGADO')