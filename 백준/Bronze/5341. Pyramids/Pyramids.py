while True:
    total = 0
    base = int(input())
    if base == 0:
        break
    while True:
        if base == 0:
            break
        total += base
        base -= 1
    print(total)