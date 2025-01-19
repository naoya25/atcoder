def main():
    n = int(input())
    a = list(set(map(int, input().split())))
    a.sort()

    start, end = 0, n
    ans = 0
    for i in range(1, n + 1):  # i巻目の漫画
        if start < end and 0 <= start < len(a) and a[start] == i:
            start += 1
            ans += 1
        elif end - start > 1:
            end -= 2
            ans += 1
        else:
            break

    print(min(ans, 10**9))
    return


if __name__ == "__main__":
    main()
