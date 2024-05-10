def main():
    s = input()
    t = input()

    si = 0
    ans = []
    for i, ti in enumerate(t):
        if ti == s[si]:
            si += 1
            ans.append(i + 1)
    print(*ans)


if __name__ == "__main__":
    main()
