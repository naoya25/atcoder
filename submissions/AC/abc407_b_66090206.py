# URL: https://atcoder.jp/contests/abc407/submissions/66090206
# id: 66090206
# epoch_second: 1748088471
# problem_id: abc407_b
# contest_id: abc407
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 250.0
# length: 278
# result: AC
# execution_time: 56


# submitted code
def main():
    x, y = map(int, input().split())

    ans = 0
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j >= x or abs(i - j) >= y:
                ans += 1

    print(ans / 36)

    return


if __name__ == "__main__":
    main()
