from time import sleep
prnum = int(input('Informe o primeiro numero: '))
secnum = int(input('Informe o segundo numero: '))
opcao = 0
while opcao != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos numeros
[ 5 ] Sair do programa
    ''')
    opcao = int(input('>>>>>>>Qual e a sua opcao? '))
    if opcao == 1:
        soma = prnum + secnum
        print('A soma entre {} + {} da {}.'.format(prnum, secnum, soma))
    elif opcao == 2:
        produto = prnum * secnum
        print('O produto entre {} x {} da {}.'.format(prnum, secnum, produto))
    elif opcao == 3:
        if prnum > secnum:
            maior = prnum
        else:
            maior = secnum
            print('Entre {} e {} o maior valor e o {}.'.format(prnum, secnum, maior))
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        prnum = int(input('Informe o primeiro numero: '))
        secnum = int(input('Informe o segundo numero: '))
    elif opcao == 5:
        print('Finalizando....')
    else:
        print('Opcao invalida. Tente novamente.')
    print('+-+' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')