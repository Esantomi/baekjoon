N = int(input())
scores = list(map(int, input().split()))

sum = 0
for i in scores:
  sum += i / max(scores) * 100
print(sum / len(scores))