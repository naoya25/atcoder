def main():
    n = int(input())
    s = [list(input()) for _ in range(n)]

    l = max(len(si) for si in s)
    for i in range(l):
        ans = "".join(s[j][i] if i < len(s[j]) else "*" for j in range(n - 1, -1, -1))
        ans = ans.rstrip('*')
        print(ans)

    return


if __name__ == "__main__":
    main()
