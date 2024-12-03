def main():
    n, d = map(int, input().split())
    s = input()
    ans = []
    for si in s[::-1]:
        if si == "@" and d > 0:
            ans.append(".")
            d -= 1
        else:
            ans.append(si)
    print("".join(ans[::-1]))

    return


if __name__ == "__main__":
    main()
