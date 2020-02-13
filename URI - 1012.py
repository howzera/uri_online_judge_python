a, b, c = input().split(' ')

pi = 3.14159

triangulo = (a*c)/2
circulo = pi*c**2
trapezio = ((a+b)/2) * c
quadrado = b**2
retangulo = a*b

print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f} '.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))