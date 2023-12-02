n = int(input())
a_list = list(map(int, input().split()))

print(*[sum(e for e in a_list if e > a) for a in a_list])
