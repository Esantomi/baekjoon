N, M, K = map(int, input().split())

# N : 전체 카드 수
# M : 앞면에 O가 적힌 카드 수 (X는 N-M)
# K : 뒷면에 O가 적힌 카드 수 (X는 N-K)

print(min(M, K) + min(N-M, N-K))