def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    ans = float("inf")
    for i in range(k + 1):
        ans = min(ans, a[-k + i - 1] - a[i])
    print(ans)
    return


if __name__ == "__main__":
    main()
