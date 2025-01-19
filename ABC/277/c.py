from collections import defaultdict


def main():
    n = int(input())
    m = 10**9

    graph = defaultdict(list)
    for _ in range(n):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    stack = [1]
    visited = defaultdict(bool)
    ans = 1
    while stack:
        s = stack.pop()

        if visited[s]:
            continue

        visited[s] = True

        for g in graph[s]:
            stack.append(g)
            ans = max(ans, g)
    print(ans)
    return


if __name__ == "__main__":
    main()
