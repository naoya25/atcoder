def main():
    s = input()
    s_arr = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    ans = 0
    di = s.index(s_arr[0])
    for c in s_arr[1:]:
        i = s.index(c)
        ans += abs(i - di)
        di = i
    print(ans)

    return


if __name__ == "__main__":
    main()
