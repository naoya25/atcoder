from collections import deque


def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]

    directions = [(0, 1), (1, 0)]
    queue = deque([(0, 0, set([a[0][0]]))])
    ans = 0
    while queue:
        nr, nc, hist = queue.popleft()
        if nr == h - 1 and nc == w - 1:
            ans += 1
            continue

        for dr, dc in directions:
            if 0 <= nr + dr < h and 0 <= nc + dc < w and a[nr + dr][nc + dc] not in hist:
                queue.append((nr + dr, nc + dc, hist | set([a[nr + dr][nc + dc]])))

    print(ans)
    return


if __name__ == "__main__":
    main()
