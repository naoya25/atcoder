def main():
    n = int(input())
    s = [[1] for _ in range(n + 1)]
    for i in range(2, n + 1):
        s[i] = s[i - 1] + [i] + s[i - 1]
    print(*s[n])
    return


if __name__ == "__main__":
    main()
