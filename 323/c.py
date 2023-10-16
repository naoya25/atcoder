n, m = map(int, input().split())
point = list(map(int, input().split()))
current_answers = [list(input()) for _ in range(n)]

max_score = 0
scores = []
# 解いてない問題の配点
remainings = []
for i, ans in enumerate(current_answers):
    score = 0
    remaining = []
    for j, v in enumerate(ans):
        if v == 'o':
            score += point[j] + i + 1
        else:
            remaining.append(point[j] + 1)
    remaining.sort(reverse=True)
    remainings.append(remaining)
    scores.append(score)
    if max_score < score:
        max_score = score

for s, r in zip(scores, remainings):
    if s == max_score:
        print(0)
        continue
    for i, v in enumerate(r):
        s += v
        if s > max_score:
            print(i + 1)
            break

