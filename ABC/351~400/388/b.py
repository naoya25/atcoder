def main():
    n, d = map(int, input().split())
    snakes = [tuple(map(int, input().split())) for _ in range(n)]

    for k in range(1, d + 1):
        max_weight = 0
        for t, l in snakes:
            max_weight = max(max_weight, t * (l + k))
        print(max_weight)

    return


if __name__ == "__main__":
    main()
