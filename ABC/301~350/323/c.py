def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    us = []
    points = []
    for i in range(n):
        s = input()
        p = sum(a[j] if s[j] == "o" else 0 for j in range(m)) + i
        points.append(p)
        us.append([a[j] for j in range(m) if s[j] == "x"])

    max_point = max(points)
    j1 = points.count(max_point) == 1

    for i in range(n):
        gp = max_point - points[i]
        if gp == 0 and j1:
            print(0)
            continue
        us[i].sort(reverse=True)
        for j, p in enumerate(us[i]):
            gp -= p
            if gp <= 0:
                print(j + 1)
                break

    return


if __name__ == "__main__":
    main()
