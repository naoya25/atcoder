def main():
    s = input()
    ans = len(s)
    cnt = 0
    for si in s:
        if si == "0":
            cnt += 1
            if cnt == 2:
                ans -= 1
                cnt = 0
        else:
            cnt = 0
    print(ans)
    return


if __name__ == "__main__":
    main()
