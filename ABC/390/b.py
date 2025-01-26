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
