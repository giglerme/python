from jaraco.text.layouts import translate

valor = int(input('Digite um número inteiro qualquer. '))
escolha = int(input('Para qual base númerica deseja converter?'
              ' 1-bin, 2-oct, 3-hexa '))
if   escolha == 1:
    valor = bin(valor)[2:]
    print('{}'.format((valor)))
elif escolha == 2:
    print('{}'.format(oct(valor)[2:]))
elif escolha == 3:
    print('{}'.format(hex(valor)[2:]))
else:
    print('Digite um valor válido.')