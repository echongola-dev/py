from datetime import date
actual = date.today().year
totalMaior = 0
totalMenor = 0
for pess in range(1, 8):
    ano = int(input('Em que ano a {}a  pessoa nasceu? '.format(pess)))
    idade = actual - ano
    if idade >= 21:
        totalMaior += 1
    else:
        totalMenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totalMaior))
print('E tambe tivemos {} pessoas menores de idade.'.format(totalMenor))