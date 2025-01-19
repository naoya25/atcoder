def main():
    Q = int(input())

    ps = [0] * (Q + 1)  # 累積和
    front_idx = 0
    back_idx = 0
    offset = 0

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
            print(ps[idx] - offset)


if __name__ == "__main__":
    main()

# =========================================
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
