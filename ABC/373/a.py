def main():
    ans = 0
    for i in range(1, 13):
        s = input()
        if i == len(s):
            ans += 1
    print(ans)
    return


if __name__ == "__main__":
    main()
