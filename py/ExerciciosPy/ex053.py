pal = str(input('Digite uma frase: ')).strip().upper()
palavras = pal.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} e {},'.format(junto, inverso), end=' ')
if inverso == junto:
    print('Temos um palindomo!')
elif inverso != junto:
    print('A frase digitada nao e um palindromo!')

    #inverso = junto[::-1]

    # As linhas  5 e 6 podem ser substituidas com a linha 13, para fazer o codigo ficar curto.