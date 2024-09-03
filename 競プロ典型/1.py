def main():
    n, l = map(int, input().split())
    k = int(input())
    a = list(map(int, input().split()))

    def judge(x):  # 最小のピースがx以上にできるか判定
        count = 0
        cut = 0
        for i in range(n):
            if a[i] - cut >= x:
                count += 1
                cut = a[i]
            if count == k:
                return l - cut >= x

        return False

    # 二分探索
    left, right = 1, l
    while left <= right:
        mid = (left + right) // 2
        if judge(mid):
            left = mid + 1
        else:
            right = mid - 1

    print(right)


if __name__ == "__main__":
    main()
