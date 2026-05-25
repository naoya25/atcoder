def main():
    m = 10**9
    n, d = map(int, input().split())

    ans = (n * pow(n - 1, d - 1, m)) % m
    print(ans)
    return


if __name__ == "__main__":
    main()
