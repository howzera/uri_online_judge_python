NOME = input()
SALARIO = float(input())
VENDAS = float(input())

COMISSAO = (VENDAS*0.15)

TOTAL = SALARIO + COMISSAO

print('TOTAL = R$ {:.2f}' .format(TOTAL))