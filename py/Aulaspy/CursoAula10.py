# Primeira condicao Pyhon
'''
if carro.esquerda():
    bloco True
else:
    bloco false
     '''

# Condicao Complexa
'''
tempo = int(input('Quantos anos em seu carro?  '))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')
'''

#Condicao simplificada
'''
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <=else'carro velho')
print('--FIM--')
'''

# Exemplo
nome = str(input('Qual e o seu nome? '))
if nome == 'Edio Iberico Chongola':
    print('O Mr. Zamani!')
else:
    print('Seu nome e tao normal!')
print('Bom dia, {}.'.format(nome))

# Exemplo 2
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua nota foi {:.1}'.format(m))
if m >= 12.0:
    print('Sua media foi boa! PARABENS!')
else:
    print('Sua media foi mal! ESTUDE MAIS.')
# print('PARABENS' if m >= else 'Estude Mais')