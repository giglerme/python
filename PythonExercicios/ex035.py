a = int(input('Primeiro lado: '))
b = int(input('Segundo lado: '))
c = int(input('Terceiro lado: '))
if a + b > c and a + c > b and b + c > a :
    print('Essas retas podem criar um triângulo.')
else:
    print('Essas retas NÃO podem formar um triângulo.')