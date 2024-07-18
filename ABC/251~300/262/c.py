def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {i + 1: a[i] for i in range(n)}

    cnt = 0
    ans = 0
    for i in range(n):
        if i + 1 == a[i]:
            cnt += 1
            continue

        if i + 1 < a[i] and d[a[i]] == i + 1:
            ans += 1
    ans += cnt * (cnt - 1) // 2
    print(ans)
    return


if __name__ == "__main__":
    main()
