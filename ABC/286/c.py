def main():
    n, a, b = map(int, input().split())
    s = input()

    ans = float("inf")

    for ai in range(n):
        arr = [s[(ai + i) % n] for i in range(n)]
        c = a * ai
        for i in range(n // 2):
            if arr[i] != arr[-i - 1]:
                c += b
        else:
            ans = min(ans, c)
    print(ans)
    return


if __name__ == "__main__":
    main()
