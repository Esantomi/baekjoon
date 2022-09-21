T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    print(f"Case {i+1}: {M-(N-1)}")