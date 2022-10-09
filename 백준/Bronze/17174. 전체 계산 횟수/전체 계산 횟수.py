N, M = map(int, input().split())  # 100 8

cnt = N
while N:
    N = N//M  # 1//8은 0
    cnt += N
print(cnt)    # 113