def main():
    n, c = map(int, input().split())
    t = list(map(int, input().split()))
    nt = t[0]
    ans = 1

    for i in range(1, n):
        if t[i] - nt >= c:
            nt = t[i]
            ans += 1
    print(ans)

    return


if __name__ == "__main__":
    main()
