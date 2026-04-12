import math
num = math.radians(float(input('Digite o valor de um ângulo: ')))
sen = math.sin(num)
cos = math.cos(num)
tan = math.tan(num)
print('seno: {:.2f}, cosseno: {:.2f}, tangente: {:.2f}'. format(sen, cos, tan))