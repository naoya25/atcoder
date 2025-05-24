# URL: https://atcoder.jp/contests/abc406/submissions/65855092
# id: 65855092
# epoch_second: 1747483477
# problem_id: abc406_a
# contest_id: abc406
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 100.0
# length: 242
# result: AC
# execution_time: 59


# submitted code
def main():
    a, b, c, d = map(int, input().split())
    time1 = a * 60 + b
    time2 = c * 60 + d

    if time1 > time2:
        print("Yes")
    else:
        print("No")

    return


if __name__ == "__main__":
    main()
