n1 = float(input('Digite a altura da superfície: '))
n2 = float(input('Digite a largura da superfície: '))
area = n1 * n2
tinta = (area / 2)
print('Sua parede tem área de {}m², '
      'logo será necessário {}l de tinta.'.format(area,tinta))
