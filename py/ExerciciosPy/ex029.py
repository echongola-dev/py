velocidade = float(input('Qual e a velocidade actual do carro? '))
if velocidade > 80:
    print('Multado! Voce excedeu a velocidade limite permitida de 80Km/h.')
    multa  = (velocidade - 80) * 500
    print('Voce deve pagar uma multa de {} meticais'.format(multa))
print('Tenha um bom dia! Dirija com cuidado.')