# URL: https://atcoder.jp/contests/abc408/submissions/66299047
# id: 66299047
# epoch_second: 1748692999
# problem_id: abc408_a
# contest_id: abc408
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 150.0
# length: 308
# result: AC
# execution_time: 61


# submitted code
def main():
    n, s = map(int, input().split())
    t = list(map(int, input().split()))
    td = 0
    for i in range(n):
        if t[i] - td > s:
            print("No")
            return
        td = t[i]
    else:
        print("Yes")
    return


if __name__ == "__main__":
    main()
