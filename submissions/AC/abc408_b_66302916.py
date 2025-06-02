# URL: https://atcoder.jp/contests/abc408/submissions/66302916
# id: 66302916
# epoch_second: 1748693102
# problem_id: abc408_b
# contest_id: abc408
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 150.0
# length: 190
# result: AC
# execution_time: 62


# submitted code
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(set(a))
    print(len(a))
    print(*a)
    return


if __name__ == "__main__":
    main()
