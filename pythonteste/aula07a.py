n1 = int(input('Digite o primeiro valor para ser calculado: '))
n2 = int(input('Digite o segundo valor a ser calculado: '))
soma = n1 + n2
subt = n1 - n2
mult = n1 * n2
divs = n1 / n2
pote = n1 ** n2
divint = n1 // n2
divres = n1 % n2
print('=' * 20)
print('Soma: {}'.format(soma), end=' ')
print('Subtração: {}'.format(subt))
print('Multiplicação: {}'.format(mult))
print('Divisão: {:.2f}'.format(divs))
print('Potência: {}'.format(pote))
print('Divisão inteira: {}'.format(divint))
print('Resto da divisão: {}'.format(divres))
print('=' * 20)
