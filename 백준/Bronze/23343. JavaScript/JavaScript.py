x, y = input().split()

print(int(x) - int(y) if x.isdigit() == 1 and y.isdigit() == 1 else 'NaN')