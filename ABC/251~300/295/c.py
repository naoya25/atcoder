def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    ans = set()
    for i in range(n - 1):
        if i in ans:
            continue
        if a[i] == a[i + 1]:
            ans.add(i)
            ans.add(i + 1)
    print(len(ans) // 2)
    return


if __name__ == "__main__":
    main()
