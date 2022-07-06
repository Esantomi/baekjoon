while True:
  N = input()
  if N == '0':
    break
  width = len(N) + 1
  for i in N:
    if i == '0':
      width += 4
    elif i ==  '1':
      width += 2
    else:
      width += 3
  print(width)