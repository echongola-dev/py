n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno e {:.1f}.'.format(n1, n2, media))
if media < 5 :
    print('E com media {:.1f}, aluno REPROVADO.'.format(media))
elif media >=5 and media < 7:
    print('E com  media {:.1f}, aluno em Recuperacao.'.format(media))
elif media >= 7:
    print('E com essa media {:.1f}, o aluno e APROVADO.'.format(media))

# Na parte de Aluno em recuperacao podemos colocar tambem >>> 7 > media >=5: