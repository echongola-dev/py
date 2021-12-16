from datetime import date
actual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = actual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificacao: MIRIM')
elif idade <= 14:
    print('Classificacao: INFANTIL')
elif idade <= 14:
    print('Claaificacao: JUNIOR.')
elif idade <= 25:
    print('Classificacao: SENIOR')
else:
    print('Classsificacao: MASTER') 

    # We can replace else with:
    # elif 