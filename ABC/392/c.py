def main():
    n = int(input())
    p = list(map(lambda x: int(x) - 1, input().split()))
    q = list(map(lambda x: int(x) - 1, input().split()))

    ans = [0] * n
    for i in range(n):
        ans[q[i]] = q[p[i]] + 1
    print(*ans)

    return


if __name__ == "__main__":
    main()
