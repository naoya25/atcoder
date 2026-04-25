def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))

    if n <= m:
        print(0)
        return

    x.sort()

    diffs = []
    for i in range(1, n):
        diffs.append(x[i] - x[i - 1])

    # 距離が小さい順に n - m 個だけ使う
    diffs.sort()
    print(sum(diffs[: n - m]))
    return


if __name__ == "__main__":
    main()
