# URL: https://atcoder.jp/contests/abc389/submissions/61830948
# id: 61830948
# epoch_second: 1737206966
# problem_id: abc389_c
# contest_id: abc389
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 807
# result: TLE
# execution_time: 2212


# submitted code
from collections import deque


def main():
    q = int(input())
    snake_lengths = deque([])
    head_positions = deque([])

    for _ in range(q):
        query = input().split()

        if query[0] == "1":
            l = int(query[1])
            snake_lengths.append(l)

            if not head_positions:
                head_positions.append(0)
            else:
                head_positions.append(head_positions[-1] + snake_lengths[-2])

        elif query[0] == "2":
            m = snake_lengths.popleft()
            head_positions.popleft()

            for i in range(len(head_positions)):
                head_positions[i] -= m

        else:
            k = int(query[1]) - 1
            print(head_positions[k])


if __name__ == "__main__":
    main()
