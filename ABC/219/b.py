def main():
    s = [input() for _ in range(3)]
    t = input()
    ans = ""
    for ti in t:
        ans += s[int(ti) - 1]
    print(ans)
    return


if __name__ == "__main__":
    main()
