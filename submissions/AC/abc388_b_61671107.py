# URL: https://atcoder.jp/contests/abc388/submissions/61671107
# id: 61671107
# epoch_second: 1736816846
# problem_id: abc388_b
# contest_id: abc388
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 200.0
# length: 344
# result: AC
# execution_time: 64


# submitted code
def main():
    n, d = map(int, input().split())
    snakes = [tuple(map(int, input().split())) for _ in range(n)]

    for k in range(1, d + 1):
        max_weight = 0
        for t, l in snakes:
            max_weight = max(max_weight, t * (l + k))
        print(max_weight)

    return


if __name__ == "__main__":
    main()
