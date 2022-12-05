tmp = [int(input()) for _ in range(5)]

scores = 0
for i in tmp:
    if i < 40:
        scores += 40
    else:
        scores += i

print(scores // 5)