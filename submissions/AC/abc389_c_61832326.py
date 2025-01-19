# URL: https://atcoder.jp/contests/abc389/submissions/61832326
# id: 61832326
# epoch_second: 1737207206
# problem_id: abc389_c
# contest_id: abc389
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 300.0
# length: 756
# result: AC
# execution_time: 176


# submitted code
def main():
    Q = int(input())

    ps = [0] * (Q + 1)  # 累積和
    front_idx = 0
    back_idx = 0
    offset = 0
    answers = []

    for _ in range(Q):
        query = input().split()
        t = int(query[0])

        if t == 1:
            l = int(query[1])
            back_idx += 1
            ps[back_idx] = ps[back_idx - 1] + l

        elif t == 2:
            removed_length = ps[front_idx + 1] - ps[front_idx]
            offset += removed_length
            front_idx += 1

        else:
            k = int(query[1])
            idx = front_idx + (k - 1)
            coord = ps[idx] - offset
            answers.append(str(coord))

    print("\n".join(answers))


if __name__ == "__main__":
    main()
