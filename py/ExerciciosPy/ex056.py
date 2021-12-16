somaIdade = 0 
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher20 = 0
for p in range(1, 5):
    print('_____ {}a PESSOA _____'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 +=1
mediaIdade = somaIdade / 4
print('A media de idade do grupo e de {} anos'.format(mediaIdade))
print('O Homem mais velho tem {} anos e se chama {}.'.format(maiorIdadeHomem, nomeVelho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totMulher20))