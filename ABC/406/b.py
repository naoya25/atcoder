def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    current = 1
    for ai in a:
        current *= ai
        if current >= 10**k:
            current = 1

    print(current)

    return


if __name__ == "__main__":
    main()
