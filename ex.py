lst = [*'abcdefghijklmnopqrstuvwxyz']
for i in lst:
  for j in lst:
    if i == j:
      continue
    print(i,j)