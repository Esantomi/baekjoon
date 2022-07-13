N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
for i in range(N):           # 첫 번째 카드
  for j in range(i+1, N):    # 두 번째 카드
    for k in range(j+1, N):  # 세 번째 카드
      total = cards[i] + cards[j] + cards[k]  # 세 카드 수의 합
      if total > M:
        continue
      else:
        result = max(result, total)

print(result)