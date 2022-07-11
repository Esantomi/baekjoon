N = input()
F = int(input())

for i in range(0, 100):
  if len(str(i)) == 1:
    i = '0' + str(i)
  n = int(N[0:-2] + str(i))
  if n % F == 0:
    print(i)
    break