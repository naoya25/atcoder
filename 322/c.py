n, m = map(int, input().split())
stack = sorted(list(map(int, input().split())), reverse=True)

for i in range(1, n + 1):
  if i == stack[-1]:
    stack.pop()
    print(0)
  else:
    print(stack[-1] - i)
