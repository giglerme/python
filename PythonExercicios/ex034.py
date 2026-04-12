sal = float(input('Qual o salário do contratado? '))
if sal <= 1250 :
    print('Novo salário é de: R${}'.format(sal + sal * 0.15))
else:
    print('Novo salário é de: R${}'.format(sal + sal * 0.1))