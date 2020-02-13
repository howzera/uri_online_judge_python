N = int(input())

ANO  = (N/365)
MES  = (N % 365)/30
DIAS = (N % 365)%30

print('{} ano(s)'.format(int(ANO)))
print('{} mes(es)'.format(int(MES)))
print('{} dia(s)'.format(int(DIAS)))