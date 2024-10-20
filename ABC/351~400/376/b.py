def main():
    n, q = map(int, input().split())
    l, r = 1, 2
    count = 0

    for _ in range(q):
        h, t = input().split()
        t = int(t)

        if h == "L":
            if t == l:
                continue

            if min(l, r) < t < max(l, r):
                distance = abs(l - t)
            else:
                if l < r:
                    if r < t:
                        distance = l + (n - t)
                    else:
                        distance = l - t
                else:
                    if l < t:
                        distance = t - l
                    else:
                        distance = t + (n - l)

            count += distance
            l = t

        elif h == "R":
            if t == r:
                continue
            if min(l, r) < t < max(l, r):
                distance = abs(r - t)
            else:
                if r < l:
                    if l < t:
                        distance = r + (n - t)
                    else:
                        distance = r - t
                else:
                    if r < t:
                        distance = t - r
                    else:
                        distance = t + (n - r)

            count += distance
            r = t

    print(count)


if __name__ == "__main__":
    main()
