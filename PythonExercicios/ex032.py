from datetime import date
ano = int(input('Qual ano gostaria de saber se é ou não bissexto? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano != 100 or ano % 400 == 0 :
    print('{} é bissexto'.format(ano))
else:
    print('{} não é bissexto'.format(ano))