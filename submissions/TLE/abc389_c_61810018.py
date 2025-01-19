# URL: https://atcoder.jp/contests/abc389/submissions/61810018
# id: 61810018
# epoch_second: 1737203600
# problem_id: abc389_c
# contest_id: abc389
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 453
# result: TLE
# execution_time: 2223


# submitted code
from collections import deque


def main():
    q = int(input())

    queue = deque([])
    for _ in range(q):
        query = input().split()
        if query[0] == "1":
            l = int(query[1])
            queue.append(l)
        elif query[0] == "2":
            m = queue.popleft()
        else:
            k = int(query[1])
            print(sum(list(queue)[: k - 1]))
    return


if __name__ == "__main__":
    main()
