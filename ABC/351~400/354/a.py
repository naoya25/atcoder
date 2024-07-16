def main():
    h = int(input())
    ans = 0
    l = 0
    while l <= h:
        l += 2**ans
        # print(l)
        ans += 1
    print(ans)
    return


if __name__ == "__main__":
    main()
