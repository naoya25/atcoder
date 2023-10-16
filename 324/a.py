n = int(input())
a = list(map(int, input().split()))

print('Yes' if all(i == a[0] for i in a) else 'No')
