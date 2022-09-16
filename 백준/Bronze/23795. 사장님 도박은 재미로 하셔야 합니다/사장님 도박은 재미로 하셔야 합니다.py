total = 0
while 1:
    money = int(input())
    if money == -1:
        break
    else:
        total += money
print(total)