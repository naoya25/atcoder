from itertools import combinations

numbers = list(range(10))
ans_list = []
for r in range(11):
    for combo in combinations(numbers, r):
        ans_list.append("".join(map(str, sorted(combo, reverse=True))))

ans_list = sorted(list(map(int, ans_list[1:])))

print(ans_list[int(input())])
