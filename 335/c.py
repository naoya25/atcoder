def main():
    n, q = map(int, input().split())
    dragon = [[n - i, 0] for i in range(n)]  # x,y
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    for _ in range(q):  # 2*10^5
        id, query = input().split()
        if id == "1":
            c = query
            dx, dy = directions[c]
            dragon_hx, dragon_hy = dragon[-1]
            dragon.append([dragon_hx + dx, dragon_hy + dy])
        else:
            p = int(query)
            print(*dragon[-p])


if __name__ == "__main__":
    main()
