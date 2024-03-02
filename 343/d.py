from collections import Counter


def main():
    n, t = map(int, input().split())
    player_goals = [0] * n  # 各選手の得点
    counts = Counter({0: n})  # 各得点のとこに何人いるか

    for _ in range(t):
        a, b = map(int, input().split())
        counts[player_goals[a - 1]] -= 1
        player_goals[a - 1] += b
        counts[player_goals[a - 1]] += 1
        ans = sum(1 for v in counts.values() if v != 0)  # こいつが重そう
        print(ans)


if __name__ == "__main__":
    main()
