def main():
    n, k = map(int, input().split())
    s = input()
    count = 0
    ans = 0
    for si in s:
        if si == "X":
            count = 0
            continue
        count += 1
        if count == k:
            ans += 1
            count = 0
    print(ans)
    return


if __name__ == "__main__":
    main()
