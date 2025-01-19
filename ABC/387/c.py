import sys

sys.setrecursionlimit(10**7)

from functools import lru_cache


# n以下のヘビ数の個数
def count_snake(n):
    if n < 10:
        return 0

    digits = list(map(int, str(n)))
    length = len(digits)

    # dp(pos, is_less, leading_digit, used_leading, used_any_other)
    # pos: 現在の桁
    # is_less: nより小さいか
    # leading_digit: 先頭桁を -1(まだ未確定) 〜 9(確定済み)
    # used_leading: 先頭を既に置いたか
    # used_any_other: 先頭以降の桁を少なくとも1つ置いたか

    @lru_cache(None)
    def dfs(pos, is_less, leading_digit, used_leading, used_any_other):
        if pos == length:
            return 1 if used_any_other and used_leading else 0

        res = 0
        limit = digits[pos] if not is_less else 9

        for d in range(limit + 1):
            nxt_is_less = is_less or (d < limit)

            if not used_leading:
                if d == 0:
                    res += dfs(pos + 1, nxt_is_less, -1, False, False)
                else:
                    res += dfs(pos + 1, nxt_is_less, d, True, False)
            else:
                if d < leading_digit:
                    res += dfs(pos + 1, nxt_is_less, leading_digit, True, True)
                else:
                    continue

        return res

    return dfs(0, False, -1, False, False)


def main():
    l, r = map(int, input().split())

    if l <= 0:
        ans = count_snake(r)
    else:
        ans = count_snake(r) - count_snake(l - 1)
    print(ans)


if __name__ == "__main__":
    main()
