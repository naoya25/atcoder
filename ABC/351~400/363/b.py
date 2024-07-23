def main():
    n, t, p = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    print(max(0, t - l[-p]))
    return


if __name__ == "__main__":
    main()
