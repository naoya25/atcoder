# URL: https://atcoder.jp/contests/abc390/submissions/62038077
# id: 62038077
# epoch_second: 1737807089
# problem_id: abc390_a
# contest_id: abc390
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 315
# result: WA
# execution_time: 55


# submitted code
def main():
    a = list(map(int, input().split()))
    n = len(a)
    for i in range(n - 1):
        a[i], a[i + 1] = a[i + 1], a[i]
        if a == sorted(a):
            print("Yes")
            return
        a[i], a[i + 1] = a[i + 1], a[i]
    print("NO")


if __name__ == "__main__":
    main()
