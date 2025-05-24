# URL: https://atcoder.jp/contests/abc406/submissions/65864448
# id: 65864448
# epoch_second: 1747483834
# problem_id: abc406_b
# contest_id: abc406
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 200.0
# length: 285
# result: AC
# execution_time: 61


# submitted code
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    current = 1
    for ai in a:
        current *= ai
        if current >= 10**k:
            current = 1

    print(current)

    return


if __name__ == "__main__":
    main()
