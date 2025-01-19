# URL: https://atcoder.jp/contests/abc388/submissions/61671230
# id: 61671230
# epoch_second: 1736817372
# problem_id: abc388_c
# contest_id: abc388
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 354
# result: TLE
# execution_time: 2218


# submitted code
def main():
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    dj = 1
    for i in range(n):
        for j in range(max(i + 1, dj), n):
            if a[i] * 2 <= a[j]:
                dj = j
                cnt += n - j
                break
    print(cnt)
    return


if __name__ == "__main__":
    main()
