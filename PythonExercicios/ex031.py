dist = float(input('Qual é a distância da viagem? '))
if dist <= 200:
    valor = (dist * 0.5)
    print('Valor da passagem: R${}'.format(valor))
else:
    valor = (dist * 0.45)
    print('Valor da passagem: R${:.2f}.'.format(valor))