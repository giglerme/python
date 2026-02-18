viagem = float(input('Qual a distância da sua viagem? '))
preço = viagem * .5 if viagem <= 200 else viagem * .45
print('Valor total: R${:.2f}'.format(preço))