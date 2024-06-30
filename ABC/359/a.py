def main():
    n = int(input())
    ans = 0
    for _ in range(n):
        s = input()
        if s == "Takahashi":
            ans += 1
    print(ans)
    return


if __name__ == "__main__":
    main()
