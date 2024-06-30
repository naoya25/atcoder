def main():
    k = int(input())
    ans = ""
    for i in range(60):
        if k & 1 << i:
            ans = "2" + ans
        else:
            ans = "0" + ans

    print(int(ans))


if __name__ == "__main__":
    main()
