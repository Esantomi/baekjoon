word = input()  # WA

alphabets = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

t = 0
for i in word:         # 'W', 'A'
  for j in alphabets:  # 'ABC', 'DEF' ...
    if i in j:         # 'W' in 'WXYZ'
      t += alphabets.index(j) + 3
print(t)