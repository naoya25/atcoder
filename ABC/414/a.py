def main():
    n, l, r = map(int, input().split())
    ans = 0
    for i in range(n):
        x, y = map(int, input().split())
        if x <= l and y >= r:
            ans += 1
    print(ans)
    return


if __name__ == "__main__":
    main()
