# URL: https://atcoder.jp/contests/abc390/submissions/62074731
# id: 62074731
# epoch_second: 1737809444
# problem_id: abc390_d
# contest_id: abc390
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 400.0
# length: 1166
# result: AC
# execution_time: 1257


# submitted code
import sys

sys.setrecursionlimit(10**7)


def main():
    n = int(input())
    a = list(map(int, input().split()))

    full_mask = 1 << n
    sumAll = [0] * full_mask
    for mask in range(full_mask):
        s = 0
        for i in range(n):
            if mask & (1 << i):
                s += a[i]
        sumAll[mask] = s

    dp = {}

    def solveDP(mask: int):
        if mask == 0:
            return {0}

        if mask in dp:
            return dp[mask]

        res = set()
        least_bit = mask & -mask
        p = least_bit.bit_length() - 1

        rest = mask ^ (1 << p)

        def submasks_of(x):
            sub = x
            while True:
                yield sub
                if sub == 0:
                    break
                sub = (sub - 1) & x

        for x in submasks_of(rest):
            T = x | (1 << p)
            block_sum = sumAll[T]

            for val in solveDP(mask ^ T):
                res.add(val ^ block_sum)

        dp[mask] = res
        return res

    ans_set = solveDP((1 << n) - 1)
    print(len(ans_set))


if __name__ == "__main__":
    main()
