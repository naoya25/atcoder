def main():
    h, w = map(int, input().split())
    q = int(input())
    grid = [[False] * (w + 1) for _ in range(h + 1)]

    def is_reachable(ra, ca, rb, cb):
        stack = [(ra, ca)]
        visited = [[False] * (w + 1) for _ in range(h + 1)]
        visited[ra][ca] = True
        while stack:
            r, c = stack.pop()
            if r == rb and c == cb:
                return True
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (
                    1 <= nr <= h
                    and 1 <= nc <= w
                    and grid[nr][nc]
                    and not visited[nr][nc]
                ):
                    visited[nr][nc] = True
                    stack.append((nr, nc))
        return False

    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            r, c = query[1], query[2]
            grid[r][c] = True
        else:
            ra, ca, rb, cb = query[1:]
            if not grid[ra][ca] or not grid[rb][cb]:
                print("No")
                continue
            if not is_reachable(ra, ca, rb, cb):
                print("No")
                continue

            print("Yes")

    return


if __name__ == "__main__":
    main()
