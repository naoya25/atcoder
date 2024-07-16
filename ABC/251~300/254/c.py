def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(a)

    for i in range(k):
        a[i::k] = sorted(a[i::k])
    print("Yes" if a == b else "No")


if __name__ == "__main__":
    main()
