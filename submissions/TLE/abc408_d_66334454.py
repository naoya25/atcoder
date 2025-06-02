# URL: https://atcoder.jp/contests/abc408/submissions/66334454
# id: 66334454
# epoch_second: 1748694856
# problem_id: abc408_d
# contest_id: abc408
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 524
# result: TLE
# execution_time: 2223


# submitted code
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        calc(n, s)

    return


def calc(n, s):
    if s.count("1") == 0:
        print(0)
        return
    ans = n
    for l in range(n):
        for r in range(l, n):
            out_ones = s[:l].count("1") + s[r + 1 :].count("1")
            in_zeros = s[l : r + 1].count("0")
            ans = min(ans, out_ones + in_zeros)
    print(ans)
    return


if __name__ == "__main__":
    main()
