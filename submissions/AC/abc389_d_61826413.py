# URL: https://atcoder.jp/contests/abc389/submissions/61826413
# id: 61826413
# epoch_second: 1737206137
# problem_id: abc389_d
# contest_id: abc389
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 400.0
# length: 282
# result: AC
# execution_time: 78


# submitted code
def main():
    r = int(input())
    j = r - 1
    quadrant = 0
    for i in range(1, r):
        while r**2 < (i + 0.5) ** 2 + (j + 0.5) ** 2:
            j -= 1
        quadrant += j

    print((r - 1) * 4 + 1 + quadrant * 4)


if __name__ == "__main__":
    main()
