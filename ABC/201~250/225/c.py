def main():
    n, m = map(int, input().split())

    for i in range(n):
        r = list(map(int, input().split()))
        if i == 0 and (r[-1] - 1) % 7 - (r[0] - 1) % 7 != m - 1:
            print("No")
            return

        # 縦チェック
        if i == 0:
            r0 = r[0]
        elif r0 + 7 != r[0]:
            print("No")
            return

        # 横が連続かどうか
        for j in range(m - 1):
            if r[j + 1] != r[j] + 1:
                print("No")
                return

        r0 = r[0]

    if r[-1] > 7 * 10**100:
        print("No")
        return

    print("Yes")
    return


if __name__ == "__main__":
    main()
