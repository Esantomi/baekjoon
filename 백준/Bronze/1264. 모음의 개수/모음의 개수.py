while True:
  s = input().lower()
  v = ['a', 'e', 'i', 'o', 'u']  # 모음 목록
  total = 0
  for i in v:
    total += s.count(i)
  if s == '#':
    break
  print(total)