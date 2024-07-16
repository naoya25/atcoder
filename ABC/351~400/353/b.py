def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))[::-1]
    aki = k
    ans = 0
    while a:
        p = a.pop()
        if aki >= p:
            aki -= p
        else:
            aki = k - p
            ans += 1
    ans += 1
    print(ans)


if __name__ == "__main__":
    main()
