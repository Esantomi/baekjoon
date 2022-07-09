# n과 n의 각 자리수를 더하는 함수 d(n) 정의
def d(n: int) -> int:
  digits = map(int, str(n))
  return n + sum(digits)

# 생성자 n이 있는 수는 셀프 넘버가 아님
non_self_nums = set()
for i in range(1, 10001):
  non_self_nums.add(d(i))  # set 원소 추가

# 비-셀프 넘버가 아니라면 셀프 넘버
for i in range(1, 10001):
  if i not in non_self_nums:
    print(i)