l_input = list(input().split())  # 734 893
for i in l_input:
  l_0 = list(reversed(l_input[0]))  # ['4', '3', '7']
  l_1 = list(reversed(l_input[1]))  # ['3', '9', '8']
if int(''.join(l_0)) > int("".join(l_1)):
  print(int(''.join(l_0)))
else:
  print(int(''.join(l_1)))

# ''.join(list) : list 요소를 하나의 문자열로 합쳐서 반환