L, P = map(int, input().split())                # 5 20
participants = list(map(int, input().split()))  # 99 101 1000 0 97

arr = []  # [-1, 1, 900, -100, -3]
for i in participants:
  arr.append(i - (L * P))

print(*arr)  # -1, 1, 900, -100, -3

# list comprehension 활용
# print(*(i - L * P for i in participants))  # -1, 1, 900, -100, -3