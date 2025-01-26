# URL: https://atcoder.jp/contests/abc390/submissions/62052000
# id: 62052000
# epoch_second: 1737807703
# problem_id: abc390_b
# contest_id: abc390
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 200.0
# length: 447
# result: AC
# execution_time: 61


# submitted code
import math


def main():
    n = int(input())
    a = list(map(int, input().split()))

    if n <= 2:
        print("Yes")
        return

    p = a[1]  # 分子
    q = a[0]  # 分母

    # 既約分数
    g = math.gcd(p, q)
    p //= g
    q //= g

    for i in range(2, n):
        if a[i] * q != a[i - 1] * p:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
