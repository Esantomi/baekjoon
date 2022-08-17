import sys
input = sys.stdin.readline

# matrix A
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]  # list comprehension

# matrix B
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

# >>> A
# [[1, 2], [3, 4], [5, 6]]
# >>> B
# [[-1, -2, 0], [0, 0, 3]]

# 3X3 zero matrix
C = [[0 for _ in range(K)] for _ in range(N)]

# >>> C
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# matrix multiplication
for n in range(N):
  for k in range(K):
    for m in range(M):
      C[n][k] += A[n][m] * B[m][k]

# >>> C
# [[-1, -2, 6], [-3, -6, 12], [-5, -10, 18]]

# print
for i in C:
  for j in i:
    print(j, end = ' ')
  print()