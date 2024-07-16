from collections import deque


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()

    total_cost = 0
    a = deque(a)

    for bi in b:
        found = False
        while a:
            ai = a.popleft()
            if ai >= bi:
                total_cost += ai
                found = True
                break
        if not found:
            print(-1)
            return

    print(total_cost)


if __name__ == "__main__":
    main()
