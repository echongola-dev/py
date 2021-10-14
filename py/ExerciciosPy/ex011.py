larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem {} x {} e a sua area e de {}m'.format(larg, alt, area))
tinta = area / 2
print('Pra pintar essa parede, voce precisara de {}l de tinta'.format(tinta))