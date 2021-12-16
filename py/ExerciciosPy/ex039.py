from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade =  atual - nasc
print('Quem nasceu  em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Voce tem que se RECENCIAR IMEDIATAMENTE.')
elif idade < 18:
    anosRem1 = 18 - idade
    print('Ainda 18 anos. Ainda faltam {} anos para o recenciamento.'.format(anosRem1))
    ano1 = atual + anosRem1
    print('O seu recenciamento sera em {}.'.format(ano1))
elif idade > 18:
    anosRem2 = idade - 18
    print('Voce deveria ter se recenciano ha {} anos.'.format(anosRem2))
    ano2 = atual - anosRem2
    print('O seu recenciamento foi em {}.'.format(ano2))
