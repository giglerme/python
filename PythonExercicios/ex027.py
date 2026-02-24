nome  = input('Digite seu nome completo: ').title().strip()
print('Olá, {}, seja bem-vindo(a).'.format(nome))
nome = nome.split()
pnome = nome[0]
unome = nome[-1]
print('Primeiro nome: {}'.format(pnome))
print('Último nome: {}'.format(unome))
print(nome[len(nome)-1])