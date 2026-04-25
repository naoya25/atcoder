from collections import Counter


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        solve(n, a)
    return


def solve(n, a):
    a.sort(key=abs)
    if n < 2:
        print("Yes")
        return

    # 絶対値が等比数列
    for i in range(1, n - 1):
        if a[i] ** 2 != a[i - 1] * a[i + 1]:
            break
    else:
        print("Yes")
        return

    # [1, -1, 1, -1] みたいなパターン
    count = Counter(a)
    if len(count) == 2:
        (x, cx), (y, cy) = count.items()
        if x + y == 0 and abs(cx - cy) <= 1:
            print("Yes")
            return
    print("No")
    return


if __name__ == "__main__":
    main()
