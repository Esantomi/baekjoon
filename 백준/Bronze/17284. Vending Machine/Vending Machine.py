btns = map(int, input().split())

money = 5000
for i in btns:
    if money < 500:
        break
    elif i == 1:
        money -= 500
    elif i == 2:
        money -= 800
    elif i == 3:
        money -= 1000
print(money)