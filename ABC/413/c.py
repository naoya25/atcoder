from collections import deque


def main():
    q = int(input())
    dq = deque()

    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            c, x = query[1], query[2]
            dq.append([c, x])
        else:
            k = query[1]
            total = 0
            while k > 0:
                c, x = dq[0]
                take = min(c, k)
                total += take * x
                k -= take
                c -= take
                if c == 0:
                    dq.popleft()
                else:
                    dq[0][0] = c
            print(total)


if __name__ == "__main__":
    main()
