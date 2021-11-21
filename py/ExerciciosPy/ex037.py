# Escreve um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de convercao.

num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para a convercao:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print('{} convertido para BINARIO e igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL e igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL e igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opcao invalida. Tente as opcoes referidas.')
