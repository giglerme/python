import random
num = random.randint(1,5)
escolha = int(input('Tente adivinhar o número entre 1 à 5 que estou pensando.'))
if escolha == num:
    print('Acertou, Parabéns.')
else:
    print('Errou')