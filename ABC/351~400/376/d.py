from collections import deque, defaultdict


def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    queue = deque([(1, 0)])
    visited = set()

    min_cycle_length = float("inf")

    while queue:
        current, length = queue.popleft()

        if current in visited:
            continue
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor == 1:
                min_cycle_length = min(min_cycle_length, length + 1)
            else:
                queue.append((neighbor, length + 1))

    if min_cycle_length == float("inf"):
        print(-1)
    else:
        print(min_cycle_length)


if __name__ == "__main__":
    main()
