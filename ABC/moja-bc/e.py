def main():
    n = int(input())
    a = [0] + list(map(lambda x: int(x) - 1, input().split()))

    graph = [[] for _ in range(n + 1)]
    for i in range(1, n):
        boss = a[i]
        graph[boss].append(i)

    ans = [0] * (n + 1)

    stack = [0]
    order = []

    while stack:
        c_emp = stack.pop()
        order.append(c_emp)

        for child in graph[c_emp]:
            stack.append(child)

    for c_emp in reversed(order):
        count = 0

        for child in graph[c_emp]:
            count += ans[child] + 1

        ans[c_emp] = count

    print(*ans[:n])


if __name__ == "__main__":
    main()
