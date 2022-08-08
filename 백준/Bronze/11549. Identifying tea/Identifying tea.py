T = int(input())
arr = map(int, input().split())

cnt = 0
for i in arr:
  cnt += 1 if i == T else 0

print(cnt)