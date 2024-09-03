def main():
    def judge():
        return True

    # 二分探索
    left, right = 1, 10**9
    while left <= right:
        mid = (left + right) // 2
        if judge(mid):
            left = mid + 1
        else:
            right = mid - 1
    print(right)
    return


if __name__ == "__main__":
    main()
