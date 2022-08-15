while 1:
  name, age, wt = input().split()
  age, wt = int(age), int(wt)
  if name == '#' and age == 0 and wt == 0:
    break
  elif age > 17 or wt >= 80:
    print(name + ' ' + 'Senior')
  else:
    print(name + ' ' + 'Junior')