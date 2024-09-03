def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    cnt = 0
    while sum(1 for x in a if x > 0) > 1:
        a.sort(reverse=True)
        a[0] -= 1
        a[1] -= 1
        cnt += 1
    print(cnt)

    return


if __name__ == "__main__":
    main()
