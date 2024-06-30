def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(2 * n - 2):
        if a[i] == a[i + 2]:
            ans += 1
    print(ans)

    return


if __name__ == "__main__":
    main()
