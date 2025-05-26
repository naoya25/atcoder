# URL: https://atcoder.jp/contests/abc407/submissions/66083278
# id: 66083278
# epoch_second: 1748088222
# problem_id: abc407_a
# contest_id: abc407
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 150.0
# length: 216
# result: AC
# execution_time: 60


# submitted code
def main():
    a, b = map(int, input().split())
    c = a / b
    d = a // b
    if c - d > d + 1 - c:
        print(d + 1)
    else:
        print(d)
    return


if __name__ == "__main__":
    main()
