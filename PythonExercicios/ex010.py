rs = float(input('Valor para converter em dólares: '))
print('R${} convertidos em Dólares fica: U${:.2f},'.format(rs, rs / 5.37), end=' ')
print('e para Euros: {}'.format(rs / 6.25))