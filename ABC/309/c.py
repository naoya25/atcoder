def main():
    n, k = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    ab.sort(reverse=True)
    # print(ab)

    if ab[0][1] > k:
        print(ab[0][0] + 1)
        return

    cnt = 0
    for i in range(n):
        cnt += ab[i][1]
        if cnt > k:
            print(ab[i][0] + 1)
            return
    print(1)
    return


if __name__ == "__main__":
    main()
