frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra a  aparece {} vezes na frase.'.format(frase.count("A")))
print('A primeira letra A apareceu na posicao {}'.format(frase.find('A')+1))
print('A Ultima letra A aparecceu na posicao {}'.format(frase.rfind('A')+1))