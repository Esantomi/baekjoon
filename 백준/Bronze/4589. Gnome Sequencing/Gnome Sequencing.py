N = int(input())

print("Gnomes:")
for _ in range(N):
  gnomes = list(map(int, input().split()))         # [91, 33, 18]
  gnomes_sorted1 = sorted(gnomes)                  # [18, 33, 91]
  gnomes_sorted2 = list(reversed(gnomes_sorted1))  # [91, 33, 18]
  if gnomes == gnomes_sorted1:
    print("Ordered")
  elif gnomes == gnomes_sorted2:
    print("Ordered")
  else:
    print("Unordered")