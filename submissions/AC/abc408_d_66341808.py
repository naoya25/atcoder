# URL: https://atcoder.jp/contests/abc408/submissions/66341808
# id: 66341808
# epoch_second: 1748695713
# problem_id: abc408_d
# contest_id: abc408
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 400.0
# length: 452
# result: AC
# execution_time: 136


# submitted code
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        calc(n, s)

    return


def calc(n, s):
    ones = s.count("1")
    if ones == 0 or ones == n:
        print(0)
        return
    best = 0
    cur = 0
    for ch in s:
        cur = max(0, cur + (1 if ch == "1" else -1))
        best = max(best, cur)

    print(ones - best)


if __name__ == "__main__":
    main()
