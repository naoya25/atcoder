def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))

    for i in range(2 * n):
        t[i % n] = min(t[i % n], t[(i - 1) % n] + s[(i - 1) % n])

    for ti in t:
        print(ti)


if __name__ == "__main__":
    main()
