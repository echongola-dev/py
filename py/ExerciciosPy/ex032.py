from datetime import date
ano = int(input('Que ano quer analisar?  Coloque 0 pra anaisar o ano actual. '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano e BISSEXTO.')
else:
    print('O ano nao e BISSEXO.') 