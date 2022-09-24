v = ['a', 'e', 'i', 'o', 'u']
word = input()
ans = list()

for i in v:
    ans.append(word.count(i))
print(sum(ans))