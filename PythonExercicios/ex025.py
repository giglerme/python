nome = input('Digite seu nome completo: ').lower().rstrip()
if nome.find('silva') == -1 :
    print('Você não tem Silva no nome.')
else:
    print('Você tem Silva no nome.')