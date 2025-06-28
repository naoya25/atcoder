def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    x = 0
    for i in range(n):
        if a[i] >= n - i:
            x = n - i
            break
    print(x)

    return


if __name__ == "__main__":
    main()
