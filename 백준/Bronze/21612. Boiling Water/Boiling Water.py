temp = int(input())
P = 5 * temp - 400

print(P)
print(1 if P < 100 else (0 if P == 100 else -1))