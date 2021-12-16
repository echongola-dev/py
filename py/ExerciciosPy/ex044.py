print('{:=^40}'.format('  LOJAS CHONGOLA  ')) 
preco = float(input('Preco das compras: MZN'))
print(''' FPRMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista cartao
[ 3 ] 2x no carato
[ 4 ] 3x ou mais no cartao''')
opcao = int(input('Qual e a opcao? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de MZN{:.2f}.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print("Sua compra sera parcelada em {}x de MZN{:.2f} COM JUROS.".format(totparc, parcela))
else:
    total = preco
    print('OPCAO INVALIDA de pagamento! tente novamene.')
print('Sua compra de MZN{:.2f}  vai custar MZN{:.2f} no final.'.format(preco, total))
