a, b, c = input().split(' ')

a=int(a)
b=int(b)
c=int(c)



d = (a+b+abs(a-b))/2

maior = (d+c+abs(d-c))/2

print('{:.0f} eh o maior'.format(maior))
