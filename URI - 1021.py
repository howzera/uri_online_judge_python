N = float(input())

notas = int(N)

moedas = (N - notas) * 100

N100 = int (notas / 100)
notas = notas % 100
N50 = int (notas / 50)
notas = notas % 50
N20 = int(notas / 20)
notas = notas % 20
N10 = int(notas / 10)
notas = notas %10
N5 = int (notas / 5)
notas = notas % 5
N2 = int(notas / 2)
notas = notas % 2

M1 = int(notas / 1)
M50 = int(moedas / 50)
moedas = moedas % 50
M25 = int(moedas / 25)
moedas = moedas % 25
M10 = int(moedas / 10)
moedas = moedas % 10
M05 = int(moedas / 5)
moedas = moedas % 5
M01 = int(moedas / 1)

print('NOTAS:')

print('{} nota (s) de R$ 100.00'.format(N100))
print('{} nota (s) de R$ 50.00'.format(N50))
print('{} nota (s) de R$ 20.00'.format(N20))
print('{} nota (s) de R$ 10.00'.format(N10))
print('{} nota (s) de R$ 5.00'.format(N5))
print('{} nota (s) de R$ 2.00'.format(N2))


print('MOEDAS:')

print('{} moeda (s) de R$ 1.00'.format(M1))
print('{} moeda (s) de R$ 0.50'.format(M50))
print('{} moeda (s) de R$ 0.25'.format(M25))
print('{} moeda (s) de R$ 0.10'.format(M10))
print('{} moeda (s) de R$ 0.05'.format(M05))
print('{} moeda (s) de R$ 0.01'.format(M01))



"""valor = float(input())

N = int(valor)

list = [100, 50, 20, 10, 5, 2]

print('{} nota(s) de R$ 100.00'.format(int(N / 100)))
aux = (N % 100)
print('{} nota(s) de R$ 50.00'.format(int(aux / 50)))
aux = (aux % 50)
print('{} nota(s) de R$ 20.00'.format(int(aux / 20)))
aux = (aux % 20)
print('{} nota(s) de R$ 10.00'.format(int(aux / 10)))
aux = (aux % 10)
print('{} nota(s) de R$ 5.00'.format(int(aux / 5)))
aux = (aux % 5)
print('{} nota(s) de R$ 2.00'.format(int(aux / 2)))
aux = (aux % 2)

print('MOEDAS:')

moedas = ((valor - N)*100)

print('{} moeda (s) de R$ 1.00'.format(int(aux / 1)))

print('{} moeda (s) de R$ 0.50'.format(int(moedas / 50)))
aux2 = moedas % 50
print('{} moeda (s) de R$ 0.25'.format(int(aux2 / 25)))
aux2 = aux2 % 25
print('{} moeda (s) de R$ 0.10'.format(int(aux2 / 10)))
aux2 = aux2 % 10
print('{} moeda (s) de R$ 0.05'.format(int(aux2 / 5)))
aux2 = aux2 % 5
print('{} moeda (s) de R$ 0.01'.format(int(aux2 / 1)))
"""