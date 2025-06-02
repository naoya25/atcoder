# URL: https://atcoder.jp/contests/abc408/submissions/66323121
# id: 66323121
# epoch_second: 1748693907
# problem_id: abc408_c
# contest_id: abc408
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 300.0
# length: 455
# result: AC
# execution_time: 182


# submitted code
def main():
    n, m = map(int, input().split())
    l = [0] * m
    r = [0] * m
    for i in range(m):
        l[i], r[i] = map(int, input().split())

    l.sort()
    r.sort()
    walls = [0] * (n + 2)
    for i in range(m):
        walls[l[i]] += 1
        walls[r[i] + 1] -= 1

    for i in range(1, n + 1):
        walls[i] += walls[i - 1]

    print(min(walls[1 : n + 1]))

    return


if __name__ == "__main__":
    main()
