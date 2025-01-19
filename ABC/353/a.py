def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i, hi in enumerate(h[1:]):
        if hi > h[0]:
            print(i + 2)
            return
    print(-1)


if __name__ == "__main__":
    main()
