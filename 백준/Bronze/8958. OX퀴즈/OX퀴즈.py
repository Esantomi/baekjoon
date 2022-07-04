T = int(input())

for _ in range(T):

  cnt = 0
  score = 0
  result = input()

  for i in result:
    if i == 'O':
      cnt += 1
      score += cnt
    else:
      cnt = 0
  print(score)