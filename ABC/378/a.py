def main():
    a = list(map(int, input().split()))
    ans = 0
    for ai in set(a):
        if a.count(ai) >=4:
            ans += 2
        elif a.count(ai) >= 2:
            ans += 1
    print(ans)
    return


if __name__ == "__main__":
    main()
