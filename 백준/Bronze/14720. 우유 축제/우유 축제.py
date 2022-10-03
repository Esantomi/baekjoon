N = int(input())
milk_st = list(map(int, input().split()))

res = 0
for i in range(N):
    if milk_st[i] == res%3:
        res +=1

print(res)