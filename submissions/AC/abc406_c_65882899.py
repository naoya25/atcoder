# URL: https://atcoder.jp/contests/abc406/submissions/65882899
# id: 65882899
# epoch_second: 1747484844
# problem_id: abc406_c
# contest_id: abc406
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 350.0
# length: 689
# result: AC
# execution_time: 123


# submitted code
def main():
    n = int(input())
    p = list(map(int, input().split()))
    if n < 4:
        return 0

    diff = [1 if p[i] < p[i + 1] else -1 for i in range(n - 1)]

    runs = []
    cur, ln = diff[0], 1
    for d in diff[1:]:
        if d == cur:
            ln += 1
        else:
            runs.append((cur, ln))
            cur, ln = d, 1
    runs.append((cur, ln))

    # +−+ 数える
    ans = 0
    for i in range(len(runs) - 2):
        s0, l0 = runs[i]
        s1, l1 = runs[i + 1]
        s2, l2 = runs[i + 2]
        if s0 == 1 and s1 == -1 and s2 == 1:
            ans += l0 * l2

    print(ans)


if __name__ == "__main__":
    main()
