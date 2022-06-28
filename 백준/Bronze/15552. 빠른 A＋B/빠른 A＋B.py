import sys

T = int(input())
for _ in range(T):
  A, B = map(int, sys.stdin.readline().split())  # input()과 동일
  print(A + B)