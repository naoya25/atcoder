def main():
    n = int(input())
    a = list(map(int, input().split()))
    sa = sorted(a, reverse=True)

    ans = a.index(sa[1]) + 1
    print(ans)

    return


if __name__ == "__main__":
    main()
