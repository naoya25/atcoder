def main():
    n, w = map(int, input().split())
    c = [list(map(int, input().split())) for _ in range(n)]
    c.sort(reverse=True)

    ans = 0
    for a, b in c:
        if w <= 0:
            break

        if w >= b:
            ans += a * b
            w -= b
        else:
            ans += a * w
            w = 0
    print(ans)
    return


if __name__ == "__main__":
    main()
