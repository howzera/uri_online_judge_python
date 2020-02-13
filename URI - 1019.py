N = int(input())

HRS = int(N/3600)
MIN = int(N%3600/60)
SEC = int(N%60)

print('{}:{}:{}'.format(HRS, MIN, SEC))