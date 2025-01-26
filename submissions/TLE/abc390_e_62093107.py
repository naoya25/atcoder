# URL: https://atcoder.jp/contests/abc390/submissions/62093107
# id: 62093107
# epoch_second: 1737811887
# problem_id: abc390_e
# contest_id: abc390
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 2302
# result: TLE
# execution_time: 2355


# submitted code
def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    vitamin1 = []
    vitamin2 = []
    vitamin3 = []
    for _ in range(n):
        v, a, c = map(int, input().split())
        if v == 1:
            vitamin1.append((a, c))
        elif v == 2:
            vitamin2.append((a, c))
        else:
            vitamin3.append((a, c))

    max1 = sum(a for a, _ in vitamin1)
    max2 = sum(a for a, _ in vitamin2)
    max3 = sum(a for a, _ in vitamin3)

    m_max = min(max1, max2, max3)

    INF = 10**15

    # dp1[v]: ビタミン1量が v 以上になるように取るときの最小カロリー
    dp1 = [INF] * (m_max + 1)
    dp1[0] = 0
    for a, c in vitamin1:
        for v in range(m_max, -1, -1):
            if dp1[v] == INF:
                continue
            nv = v + a
            if nv >= m_max:
                nv = m_max
            cost = dp1[v] + c
            if cost < dp1[nv]:
                dp1[nv] = cost

    for v in range(m_max - 1, -1, -1):
        dp1[v] = min(dp1[v], dp1[v + 1])

    # ビタミン2
    dp2 = [INF] * (m_max + 1)
    dp2[0] = 0
    for a, c in vitamin2:
        for v in range(m_max, -1, -1):
            if dp2[v] == INF:
                continue
            nv = v + a
            if nv >= m_max:
                nv = m_max
            cost = dp2[v] + c
            if cost < dp2[nv]:
                dp2[nv] = cost
    for v in range(m_max - 1, -1, -1):
        dp2[v] = min(dp2[v], dp2[v + 1])

    # ビタミン3
    dp3 = [INF] * (m_max + 1)
    dp3[0] = 0
    for a, c in vitamin3:
        for v in range(m_max, -1, -1):
            if dp3[v] == INF:
                continue
            nv = v + a
            if nv >= m_max:
                nv = m_max
            cost = dp3[v] + c
            if cost < dp3[nv]:
                dp3[nv] = cost
    for v in range(m_max - 1, -1, -1):
        dp3[v] = min(dp3[v], dp3[v + 1])

    # 二分探索
    left, right = 0, m_max + 1
    while left + 1 < right:
        mid = (left + right) // 2
        if dp1[mid] + dp2[mid] + dp3[mid] <= x:
            left = mid
        else:
            right = mid

    print(left)


if __name__ == "__main__":
    main()
