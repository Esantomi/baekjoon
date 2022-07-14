N, M = map(int, input().split())

mt1, mt2 = [], []

# 행렬 성분 대입
for mt in [mt1, mt2]:
  for _ in range(N):
    row = list(map(int, input().split()))
    mt.append(row)

# 행렬 간 덧셈
for i in range(N):
  for j in range(M):
    mt1[i][j] += mt2[i][j]
  print(*mt1[i])  # mt1 : [[4, 4, 4], [6, 6, 6], [5, 6, 100]]

# *는 list의 각 요소를 함수의 argument로 넣어 줌