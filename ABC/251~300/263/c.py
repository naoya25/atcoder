from collections import deque


def main():
    n, m = map(int, input().split())

    ans = []
    queue = deque([([i], 1) for i in range(1, m + 1)])  # ans, 桁数
    while queue:
        a, i = queue.popleft()
        if i == n:
            ans.append(a)
            continue

        for j in range(a[-1] + 1, m + 1):
            queue.append((a + [j], i + 1))

    for r in ans:
        print(*r)
    return


if __name__ == "__main__":
    main()
