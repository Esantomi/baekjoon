ones_place = int(input())
cars = list(map(int, input().split()))

cnt = 0
for i in cars:
  if i == ones_place:
    cnt += 1
print(cnt)

# print(cars.count(ones_place))가 더 간단함