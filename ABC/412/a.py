def main():
    n = int(input())
    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if a < b:
            ans += 1
    print(ans)
    return


if __name__ == "__main__":
    main()
