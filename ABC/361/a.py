def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))

    ans = []
    for i in range(n):
        ans.append(a[i])
        if i + 1 == k:
            ans.append(x)

    print(*ans)
    return


if __name__ == "__main__":
    main()
