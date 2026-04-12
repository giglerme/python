import random
num = random.randint(0,5)
escolha = int(input('Tente adivinhar o número entre 1 à 5 que estou pensando.'))
if escolha > 5:
    print('Digite um número válido. 1 à 5')
elif escolha == num:
    print('Acertou, Parabéns.')
else:
    print('Errou. Eu pensei no número {}'.format(num))