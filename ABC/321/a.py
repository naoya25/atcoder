n = input()
n_sort = sorted(list(map(int, list(n))), reverse=True)
if len(set(n_sort)) == len(n) and list(map(int, n)) == n_sort:
  print('Yes')
else:
  print('No')
