T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    candies = list(map(int, input().split()))
    kids = 0
    
    for candy in candies:
        kids += candy // K
    print(kids)