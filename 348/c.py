def main():
    n = int(input())
    beans = {}
    for _ in range(n):
        a, c = map(int, input().split())
        if c not in beans.keys():
            beans[c] = a
        else:
            beans[c] = min(beans[c], a)
    k, v = max(beans.items(), key=lambda x: x[1])
    print(v)


if __name__ == "__main__":
    main()
