import random
j1 = str(input('Primeiro aluno: '))
j2 = str(input('Segundo aluno: '))
j3 = str(input('Terceiro jogador: '))
j4 = str(input('Quarto jogador: '))
lista = [j1, j2 , j3 , j4]
escolhido = random.choice(lista)
print('O vencedor é {}'.format(escolhido))
'''vencedor = random.randint(1,4)

if vencedor == 1:
    print(j1)
elif vencedor == 2:
    print(j2)
elif vencedor == 3:
    print(j3)
else:
    print(j4)
'''