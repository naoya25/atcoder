def main():
    n = int(input())
    h = tuple(map(int, input().split()))

    max_count = 1

    for i in range(n):
        for j in range(i + 1, n):
            if h[i] != h[j]:
                continue
            count = 2
            for k in range(j + j - i, n, j - i):
                if h[k] == h[i]:
                    count += 1
                else:
                    break
            max_count = max(max_count, count)

    print(max_count)
    return


if __name__ == "__main__":
    main()
