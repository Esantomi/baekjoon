# 내 풀이 : 리스트 활용
word = input()

ans = []
for i in word:
  if i.isupper():
    ans.append(i.lower())
  else:
    ans.append(i.upper())

print(''.join(ans))


# 다른 풀이1 : 문자열 연산
# word = input()

# ans = ""
# for i in word:
#   if i.isupper():
#     ans += i.lower()
#   else:
#     ans += i.upper()

# print(ans)


# 다른 풀이2 : swapcase()
# word = input()
# print(word.swapcase())