N = input()  # 26
num = N
cnt = 0

while True:
  if len(num) == 1:
    N = "0" + N
    num = "0" + num
  sum = str(int(num[0]) + int(num[1]))  # 2 + 6
  num = num[-1] + sum[-1]  # 6 + 8
  cnt += 1
  if num == N:
    print(cnt)
    break