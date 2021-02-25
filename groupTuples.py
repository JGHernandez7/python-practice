test = [(1, 3), (1, 5), (3, 4), (3, 9), (5, 10)]
a = []

for i in test:
  if a and a[-1][0] == i[0]:
    a[-1].extend(i[1:])
  else:
    a.append([j for j in i])

a = list(map(tuple, a))

print("Original list: " + str(test));
print("Extracted elements: " + str(a));