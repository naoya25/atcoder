def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    while a[-1] - a[0] > 1:
        a[0] = a[0] + 1
        a[-1] = a[-1] - 1
        a.sort()
        ans += 1
    print(ans)

    return


if __name__ == "__main__":
    main()
