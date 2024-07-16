def main():
    n, l, r = map(int, input().split())
    arr = [r - i + l if l <= i <= r else i for i in range(1, n + 1)]
    print(*arr)

    return


if __name__ == "__main__":
    main()
