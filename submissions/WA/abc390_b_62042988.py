# URL: https://atcoder.jp/contests/abc390/submissions/62042988
# id: 62042988
# epoch_second: 1737807282
# problem_id: abc390_b
# contest_id: abc390
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 289
# result: WA
# execution_time: 62


# submitted code
def main():
    n = int(input())
    a = list(map(int, input().split()))

    ratio = a[1] / a[0]
    for i in range(1, n):
        if a[i] / a[i - 1] != ratio:
            print("No")
            return

    print("Yes")
    return


if __name__ == "__main__":
    main()
