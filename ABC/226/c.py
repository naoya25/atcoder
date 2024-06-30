def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    idx = 0
    n = int(data[idx])
    idx += 1

    t_arr = [0] * n
    a_arr = [[] for _ in range(n)]

    for i in range(n):
        t = int(data[idx])
        k = int(data[idx + 1])
        t_arr[i] = t
        a_arr[i] = [int(data[idx + 2 + j]) - 1 for j in range(k)]
        idx += 2 + k

    ha = set()
    stack = [n - 1]

    while stack:
        na = stack.pop()
        if na not in ha:
            ha.add(na)
            stack.extend(a_arr[na])

    result = sum(t_arr[i] for i in ha)
    print(result)


if __name__ == "__main__":
    main()
