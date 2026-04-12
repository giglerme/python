a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# verificando quem é o menor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(maior)
#verificando menor
menor = a
if a > b and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(menor)