n, m, p = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

count = sum([min(a+b, p) for a in a_list for b in b_list])

print(count)
