from math import sqrt, pow
catad = float(input('Digite o cateto adjacente: '))
catop = float(input('Digite o cateto oposto: '))
hip   = sqrt(pow(catad,2) + pow(catop,2))
print('{:.3f}'.format(hip))