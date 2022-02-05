# Sequencia de fibonacci #
print('=' *30)
print('Sequencia de Fibonacci')
print('=' *30)
n = int(input('Quantos termos quer mostrar? ')) # O input do numero dos termos do programa
t1 = 0 # o t1 e o t2 sao as constantes universais da sequencia de fibonacci
t2 = 1
print('~' * 30)
print('{} → {}'.format(t1, t2), end='') # O print mostra as duas duas principais constantes
cont = 3
while cont <= n:  # Equanto nao chegar no numero dos termos pedidos pelo utilzador o programa nao para de funcionar
    t3 = t1 + t2  # A Linha gera o 3 termo juntanto os dois primeiros termos com um operador aretimetrico
    print(' → {}'.format(t3), end=' ') # A linha mosta o numero gerado pela operacao da linha 12
    t1 = t2 # A linha 14 e a linha 15 fazem a transicao de posicao dos termpos.
    t2 = t3
    cont+=1
print(' → FIM')
print('~' * 30)