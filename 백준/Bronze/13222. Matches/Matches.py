N, W, H = map(int, input().split())
hyp = (W**2 + H**2)**(1/2)

for _ in range(N):
    match = int(input())
    print('YES' if match <= hyp else 'NO')