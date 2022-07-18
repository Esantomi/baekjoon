check_list = list(range(1, 31))

for _ in range(28):
  n = int(input())
  if n in check_list:
    check_list.remove(n)

print(min(check_list))
print(max(check_list))