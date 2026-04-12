#empréstimo bancário
#coletando dados
valorimovel = float(input('Quanto custa o imóvel? '))
salario     = float(input('Quanto você ganha mensalmente? '))
quantprest  = int(input('Será pago em quantos anos? '))

#processamento de dados
valorprest: float = valorimovel / (quantprest * 12)

#print de teste
print(valorprest)
#transformei em variável apenas para
calc = valorprest > (salario * 0.3)
print(calc)
if calc :
    print('Empréstimo negado.')
else:
    print('Empréstimo concedido.')

