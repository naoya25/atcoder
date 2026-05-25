def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[i] + a[j] + a[k] == x:
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
