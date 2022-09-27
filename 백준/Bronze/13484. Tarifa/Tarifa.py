X = int(input())  # 전체 용량(MB)
N = int(input())  # 달수

MB_left = 0
for _ in range(N):
    P = int(input())
    MB_left += X-P

print(MB_left + X)