def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = [(a[i], i+1) for i in range(n)]
    d.sort()
    print(d[-2][1])
    return


if __name__ == "__main__":
    main()
