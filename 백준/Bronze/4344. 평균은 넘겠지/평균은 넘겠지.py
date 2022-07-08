C = int(input())

for _ in range(C):
  nums = list(map(int, input().split()))
  avg = sum(nums[1:])/nums[0]  # 평균
  cnt = 0
  for score in nums[1:]:
    if score > avg:
      cnt += 1
  rate = cnt/nums[0] * 100
  print(f'{rate:.3f}%')  # 소수점 셋째 자리