def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if i**3 > n:
            break
        for j in range(i, n + 1):
            if i * j * j > n or n // (i * j) < j:
                break
            ans += n // (i * j) - j + 1
    print(ans)


if __name__ == "__main__":
    main()
