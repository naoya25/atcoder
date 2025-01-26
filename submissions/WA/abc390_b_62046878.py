# URL: https://atcoder.jp/contests/abc390/submissions/62046878
# id: 62046878
# epoch_second: 1737807450
# problem_id: abc390_b
# contest_id: abc390
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 332
# result: WA
# execution_time: 56


# submitted code
def main():
    n = int(input())
    a = list(map(int, input().split()))

    rn = a[1] // a[0]
    rd = a[1] % a[0]
    for i in range(1, n):
        if a[i] // a[i - 1] != rn or a[i] % a[i - 1] != rd:
            print("No")
            return

    print("Yes")
    return


if __name__ == "__main__":
    main()
