# URL: https://atcoder.jp/contests/abc389/submissions/61805626
# id: 61805626
# epoch_second: 1737203072
# problem_id: abc389_c
# contest_id: abc389
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 654
# result: WA
# execution_time: 572


# submitted code
from collections import deque


def main():
    q = int(input())

    # 累積和
    prefix = deque([])
    offset = 0

    for _ in range(q):
        query = input().split()
        if query[0] == "1":
            l = int(query[1])
            if not prefix:
                prefix.append(l)
            else:
                prefix.append(prefix[-1] + l)
        elif query[0] == "2":
            m = prefix.popleft()
            offset = m
        elif query[0] == "3":
            k = int(query[1])
            # print(prefix, offset, k)
            print(prefix[k - 2] - offset)


if __name__ == "__main__":
    main()
