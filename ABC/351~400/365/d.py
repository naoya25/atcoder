def main():
    n = int(input())
    s = input()

    s_int = {"P": 0, "R": 1, "S": 2}
    win = {"P": "S", "R": "P", "S": "R"}
    dp = [[0, 0, 0] for _ in range(n + 1)]
    """
    dp[i][j]の時
    jを確認→s[i]を確認：あいこか勝ちかわかる
    あいこの時
    1手前のjではない手のなかの最大値
    勝ちの時
    1手前のjではない手のなかの最大値+1
    負けの時
    0
    """

    for i in range(1, n + 1):
        for j in range(3):
            if j == s_int[s[i - 1]]:  # あいこ
                dp[i][j] = max(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])
            elif j == s_int[win[s[i - 1]]]:  # 勝ち
                dp[i][j] = max(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + 1
            else:  # 負け
                dp[i][j] = 0

    print(max(dp[-1]))

    return


if __name__ == "__main__":
    main()
