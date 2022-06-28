l = []
for _ in range(1, 10):
  l.append(int(input()))

print(max(l))
print(l.index(max(l)) + 1)  # l의 최댓값의 인덱스 + 1