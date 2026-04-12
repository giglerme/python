nome = input(('Digite seu nome completo: '))
saudacoes = 'Bem Vindo, '
print('-'.join(saudacoes.split()), nome.upper())
print('-'.join(saudacoes.split()), nome.title())
print(len(nome.split()[0]) + len((nome.split()[1])) + len((nome.split()[2])))
print(len(nome.split()[0]))