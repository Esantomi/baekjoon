word = input().upper()              # Mississipi -> MISSISSIPI
letters_of_word = list(set(word))   # ['S', 'P', 'I', 'M']

cnt = []  # [4, 1, 4, 1]
for i in letters_of_word:
  cnt.append(word.count(i))
  
if cnt.count(max(cnt)) > 1:
  print('?')
else:
  max_index = cnt.index(max(cnt))
  print(letters_of_word[max_index])

# find() : 없을 경우 -1 반환
# index() : 없을 경우 ValueError 반환