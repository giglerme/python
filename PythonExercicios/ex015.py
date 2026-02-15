diaalu = int(input('Por quantos dias o veículo foi alugado? '))
kmrod  = float(input('Quantos quilometros(km) foram rodados? '))
valor  = diaalu * 60 + kmrod * 0.15
print('Dias alugados:     {}'.format(diaalu))
print('Kilomtros rodados: {}'.format(kmrod))
print('Valor total:       {:.2f}'.format(valor))
