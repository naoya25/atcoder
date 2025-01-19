def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)

    ans = n
    total_a = 0
    for i in range(n):
        total_a += a[i]
        if total_a > x:
            ans = min(ans, i + 1)
            break

    total_b = 0
    for i in range(n):
        total_b += b[i]
        if total_b > y:
            ans = min(ans, i + 1)
            break
    print(ans)
    return


if __name__ == "__main__":
    main()
