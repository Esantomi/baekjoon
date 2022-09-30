N = int(input())
line = list(map(int, input().split()))
sorted_line = sorted(line)

cnt = 0
for i in range(N):
    if line[i] != sorted_line[i]:
        cnt += 1
print(cnt)