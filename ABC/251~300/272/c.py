def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    even, odd = [], []
    for ai in a:
        if ai % 2 == 0:
            even.append(ai)
        else:
            odd.append(ai)

    if n == 2 and len(even) == len(odd) == 1:
        print(-1)
        return

    ans = 0
    if len(even) >= 2:
        ans = max(ans, even[-1] + even[-2])
    if len(odd) >= 2:
        ans = max(ans, odd[-1] + odd[-2])
    print(ans)
    return


if __name__ == "__main__":
    main()
