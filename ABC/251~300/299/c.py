# def main():
#     n = int(input())
#     s = input()
#     if not ("-" in s and "o" in s):
#         print(-1)
#         return
#     print(max(map(len,s.split('-'))))
#     return


# if __name__ == "__main__":
#     main()


def main():
    n = int(input())
    s = list(input())
    if len(set(s)) < 2:
        print(-1)
        return
    ans = 0
    cnt = 0
    for si in s:
        if si == "o":
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)

    print(ans)
    return


if __name__ == "__main__":
    main()
