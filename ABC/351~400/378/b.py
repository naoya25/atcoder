def main():
    n = int(input())
    trashes = [tuple(map(int, input().split())) for _ in range(n)]
    q = int(input())
    for _ in range(q):
        t, d = map(int, input().split())
        q_, r = trashes[t - 1]

        remainder = d % q_

        if remainder <= r:
            ans = d - remainder + r
        else:
            ans = d - remainder + q_ + r

        print(ans)

if __name__ == "__main__":
    main()
