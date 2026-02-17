v = int(input('Qual é a velocidade do veículo? '))
if v <= 80:
    print('Tudo bem.😁')
else:
    m = (v - 80) * 7
    print('Levou multa de R${}.'.format(m))