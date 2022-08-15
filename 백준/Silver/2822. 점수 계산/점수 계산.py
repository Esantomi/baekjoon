scores = []
scores_sum = 0
score_indices = []

for _ in range(8):
  scores.append(int(input()))

# temp = sorted(scores, reverse = True)

for i in range(5):
  max_i = scores.index(max(scores))
  score_indices.append(max_i + 1)
  scores_sum += scores[max_i]
  scores[max_i] = 0

score_indices.sort()  # list.sort()는 원본 리스트 정렬, sorted(list)는 새 리스트 반환

print(scores_sum)
for i in score_indices:
  print(i, end = ' ')