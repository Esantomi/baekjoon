import sys
input = lambda: sys.stdin.readline().rstrip()
# sys.stdin.readline()은 우측 \n 포함

N, M = map(int, input().split())

dict = {}

for i in range(1, N+1):
  pokemon = input()
  dict[i] = pokemon
  dict[pokemon] = i

for _ in range(M):
  x = input()
  if x.isdigit():
    print(dict[int(x)])
  else:
    print(dict[x])