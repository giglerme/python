n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
nums = [n1, n2, n3].sort()

if n1 > n2 and n1 > n3 :
    print('{} é o maior número.'.format(n1))
elif n2> n3:
    print('{} é o maior número.'.format(n2))
else:
    print('{} é o maior número.'.format(n3))