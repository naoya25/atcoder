def main():
    n = int(input())
    a = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]
    # print(a)

    di = 0
    for i in range(n):
        # print(di, i)
        di = a[max(di, i)][min(di, i)]
    print(di + 1)
    return


if __name__ == "__main__":
    main()
