def main():
    n = int(input())

    if n <= 10:
        print(n - 1)
        return
    """
    0は一旦無地
    1桁の回文数: 9個
    2桁の回文数: 9個
    3桁の回文数: 90個
    4桁の回文数: 90個
    5桁の回文数: 900個
    6桁の回文数: 900個
    ...
    k桁の回文数: 9*10**((k-1)//2)個
    ...

    まず桁数を求める
    桁がもとまったらその桁のうちの何番目かを調べる
    上半分を生成して、それを元に下半分を生成して終わり
    """

    k = 1
    n -= 1
    while n > 9 * 10 ** ((k - 1) // 2):
        n -= 9 * 10 ** ((k - 1) // 2)
        k += 1

    # print(k)
    # print(n)
    hk = -(-k // 2)
    up_ans = str(10 ** (hk - 1) + n - 1)
    down_ans = up_ans[::-1]
    if k % 2 == 0:
        print(up_ans + down_ans)
    else:
        print(up_ans + down_ans[1:])


if __name__ == "__main__":
    main()
