def main():
    # 0-index
    n, q = map(int, input().split())

    above = [-1] * n
    under = [-1] * n

    for _ in range(q):
        c, p = map(lambda x: int(x) - 1, input().split())

        # 切断
        tmp_c = under[c]
        if tmp_c != -1:
            above[tmp_c] = -1

        # 乗せる
        under[c] = p
        above[p] = c

    ans = [0] * n
    for i in range(n):
        if under[i] == -1:
            count = 0
            curr = i
            while curr != -1:
                count += 1
                curr = above[curr]
            ans[i] = count
        else:
            ans[i] = 0

    print(*ans)


if __name__ == "__main__":
    main()
