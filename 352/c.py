def main():
    n = int(input())
    ans = 0
    head = 0
    for _ in range(n):
        a, b = map(int, input().split())
        head = max(head, b - a)
        ans += a
    print(ans + head)


if __name__ == "__main__":
    main()
