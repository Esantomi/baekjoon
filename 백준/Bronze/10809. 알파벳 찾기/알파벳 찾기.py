S = input()
alphabet = range(97, 123)  # 아스키코드 a-z

for i in alphabet:
  print(S.find(chr(i)))