cod1, num1, val1 = input().split(' ')
cod2, num2, val2 = input().split(' ')


total = ((int(num1) * float(val1)) + (int(num2) * float(val2)))

print('VALOR A PAGAR: R$ {:.2f}'.format(total))