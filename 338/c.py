def main():
    N = int(input())
    Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    INF = 10**18
    ans = 0
    for x in range(max(Q) + 1):
        y = INF
        for i in range(N):
            if Q[i] < A[i] * x:
                y = -INF
            elif B[i] > 0:
                y = min(y, (Q[i] - A[i] * x) // B[i])
        ans = max(ans, x + y)
    print(ans)


if __name__ == "__main__":
    main()
