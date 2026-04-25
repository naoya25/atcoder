def main():
    n = int(input())
    ans = ""
    ls = 0
    for i in range(n):
        c, l = input().split()
        l = int(l)
        ls += l
        if ls > 100:
            print("Too Long")
            return
        ans += c * l
    print(ans)
    return


if __name__ == "__main__":
    main()
