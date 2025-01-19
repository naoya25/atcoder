def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n - 2):
        if s[i] == "#" and s[i + 1] == "." and s[i + 2] == "#":
            ans += 1

    print(ans)
    return


if __name__ == "__main__":
    main()
