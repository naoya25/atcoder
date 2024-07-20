def main():
    n = int(input())
    s = input()

    ans = ""
    j = True
    for si in s:
        if si == '"':
            j = not j
        elif si == "," and j:
            si = "."
        ans += si
    print(ans)
    return


if __name__ == "__main__":
    main()
