# URL: https://atcoder.jp/contests/abc388/submissions/61717102
# id: 61717102
# epoch_second: 1736986684
# problem_id: abc388_d
# contest_id: abc388
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 400.0
# length: 417
# result: AC
# execution_time: 188


# submitted code
def main():
    n = int(input())
    a = list(map(int, input().split()))

    c = [0] * n
    d = [0] * (n + 1)

    for i in range(n):
        if i != 0:
            c[i] = c[i - 1] + d[i]
            a[i] += c[i]

        give = min(a[i], (n - i - 1))
        a[i] -= give

        d[i + 1] += 1
        d[i + give + 1] -= 1

    print(*a)
    return


if __name__ == "__main__":
    main()
