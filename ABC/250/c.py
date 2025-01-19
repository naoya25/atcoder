n, q = map(int, input().split())
ball_list = list(range(1, n + 1))
getPosition = {ball: id for id, ball in zip(range(n), range(1, n + 1))}

for _ in range(q):
    target = int(input())
    i = getPosition[target]
    if i == n - 1:
        getPosition[ball_list[i]], getPosition[ball_list[i - 1]] = i - 1, i
        ball_list[i], ball_list[i - 1] = ball_list[i - 1], ball_list[i]
    else:
        getPosition[ball_list[i]], getPosition[ball_list[i + 1]] = i + 1, i
        ball_list[i], ball_list[i + 1] = ball_list[i + 1], ball_list[i]

print(*ball_list)
