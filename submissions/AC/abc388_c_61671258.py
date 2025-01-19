# URL: https://atcoder.jp/contests/abc388/submissions/61671258
# id: 61671258
# epoch_second: 1736817520
# problem_id: abc388_c
# contest_id: abc388
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 300.0
# length: 282
# result: AC
# execution_time: 238


# submitted code
import bisect


def main():
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        j = bisect.bisect_left(a, a[i] * 2, i + 1)
        cnt += n - j

    print(cnt)
    return


if __name__ == "__main__":
    main()
