n, m = map(int, input().split())
s, t = input(), input()
score = 3 - 2 * (s == t[:n]) - (s == t[-n:])
print(score)
