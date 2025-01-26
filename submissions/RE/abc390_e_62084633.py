# URL: https://atcoder.jp/contests/abc390/submissions/62084633
# id: 62084633
# epoch_second: 1737810655
# problem_id: abc390_e
# contest_id: abc390
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 2015
# result: RE
# execution_time: 2307


# submitted code
def main():
    n, x = map(int, input().split())
    G1 = []
    G2 = []
    G3 = []
    for _ in range(n):
        v, a, c = map(int, input().split())
        if v == 1:
            G1.append((a, c))
        elif v == 2:
            G2.append((a, c))
        else:
            G3.append((a, c))

    max1 = sum(a for a, _ in G1)
    max2 = sum(a for a, _ in G2)
    max3 = sum(a for a, _ in G3)
    m_max = min(max1, max2, max3)

    # dp1[v]: ビタミン量がvのときの最小カロリー
    INF = float("inf")
    dp1 = [INF] * (max1 + 1)
    dp1[0] = 0
    for a, c in G1:
        for v in range(max1 - a, -1, -1):
            if dp1[v] == INF:
                continue
            nv = v + a
            cost = dp1[v] + c
            if cost < dp1[nv]:
                dp1[nv] = cost

    for v in range(max1 - 1, -1, -1):
        dp1[v] = min(dp1[v], dp1[v + 1])

    # ==============================
    dp2 = [INF] * (max2 + 1)
    dp2[0] = 0
    for a, c in G2:
        for v in range(max2 - a, -1, -1):
            if dp2[v] == INF:
                continue
            nv = v + a
            cost = dp2[v] + c
            if cost < dp2[nv]:
                dp2[nv] = cost
    for v in range(max2 - 1, -1, -1):
        dp2[v] = min(dp2[v], dp2[v + 1])

    # ==============================
    dp3 = [INF] * (max3 + 1)
    dp3[0] = 0
    for a, c in G3:
        for v in range(max3 - a, -1, -1):
            if dp3[v] == INF:
                continue
            nv = v + a
            cost = dp3[v] + c
            if cost < dp3[nv]:
                dp3[nv] = cost
    for v in range(max3 - 1, -1, -1):
        dp3[v] = min(dp3[v], dp3[v + 1])

    # bisect
    left = 0
    right = m_max + 1
    while left + 1 < right:
        mid = (left + right) // 2
        if dp1[mid] + dp2[mid] + dp3[mid] <= x:
            left = mid
        else:
            right = mid

    print(left)


if __name__ == "__main__":
    main()
