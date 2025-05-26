# URL: https://atcoder.jp/contests/abc407/submissions/66106452
# id: 66106452
# epoch_second: 1748089595
# problem_id: abc407_c
# contest_id: abc407
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 300.0
# length: 383
# result: AC
# execution_time: 66


# submitted code
def main():
    s = input()
    n = len(s)

    x_next = int(s[-1])
    for i in range(n - 2, -1, -1):
        si = int(s[i])
        diff = x_next - si
        if diff <= 0:
            x_curr = si
        else:
            x_curr = si + ((diff + 9) // 10) * 10
        x_next = x_curr

    print(n + x_next)

    return


if __name__ == "__main__":
    main()
