def main():
    n = int(input())
    print(1)  # 最初のターンとりあえず1宣言
    nums = set(range(2, 2 * n + 2))  # 1使ったから、2~2n+1
    while True:
        aoki = int(input())
        if aoki == 0:
            return

        nums.remove(aoki)
        takahashi = nums.pop()
        print(takahashi)

    return


if __name__ == "__main__":
    main()
