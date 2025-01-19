def main():
    n = int(input())
    cx, cy = 0, 0
    cost = 0
    for _ in range(n):
        x, y = map(int, input().split())

        cost += ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
        cx, cy = x, y
    else:
        cost += (cx**2 + cy**2) ** 0.5
    print(cost)
    return


if __name__ == "__main__":
    main()
