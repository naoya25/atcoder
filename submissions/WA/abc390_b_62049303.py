# URL: https://atcoder.jp/contests/abc390/submissions/62049303
# id: 62049303
# epoch_second: 1737807565
# problem_id: abc390_b
# contest_id: abc390
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 367
# result: WA
# execution_time: 59


# submitted code
def main():
    n = int(input())
    a = list(map(int, input().split()))

    if n <= 2:
        print("Yes")
        return

    rn = a[1] // a[0]
    rd = a[1] % a[0]
    for i in range(1, n):
        if a[i - 1] * rn + rd != a[i]:
            print("No")
            return

    print("Yes")
    return


if __name__ == "__main__":
    main()
