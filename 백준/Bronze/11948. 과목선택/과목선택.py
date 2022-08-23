sci = []
soc = []

for _ in range(4):
  sci.append(int(input()))

for _ in range(2):
  soc.append(int(input()))

sci.remove(min(sci))
print(sum(sci) + max(soc))