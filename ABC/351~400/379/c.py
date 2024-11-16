def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    a = list(map(int, input().split()))

    xa = sorted(zip(x, a), key=lambda x: x[0])

    current_sum = 0
    sum_idx = 0

    for xi, ai in xa:
        if current_sum < xi - 1:
            print(-1)
            return
        current_sum += ai
        sum_idx += xi * ai

    if current_sum != n:
        print(-1)
        return

    print(n * (n + 1) // 2 - sum_idx)


if __name__ == "__main__":
    main()
