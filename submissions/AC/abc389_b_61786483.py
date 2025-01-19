# URL: https://atcoder.jp/contests/abc389/submissions/61786483
# id: 61786483
# epoch_second: 1737201782
# problem_id: abc389_b
# contest_id: abc389
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 150.0
# length: 178
# result: AC
# execution_time: 56


# submitted code
def main():
    x = int(input())
    t = 1
    n = 1
    while n != x:
        t += 1
        n *= t
    print(t)
    return


if __name__ == "__main__":
    main()
