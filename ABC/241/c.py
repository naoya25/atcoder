def main():
    n = int(input())
    grid = [input().strip() for _ in range(n)]

    # 方向を定義 (右、左、下、上、右下、左下、右上、左上)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def in_bounds(x, y):
        return 0 <= x < n and 0 <= y < n

    for i in range(n):
        for j in range(n):
            for dr, dc in directions:
                count = 0
                black = 2  # 残りの黒に変えれるマス数
                for k in range(6):
                    ni, nj = i + dr * k, j + dc * k
                    if in_bounds(ni, nj):
                        if grid[ni][nj] == "#":
                            count += 1
                        else:
                            black -= 1
                            if black < 0:
                                break
                            count += 1
                    else:
                        break
                if count == 6:
                    print("Yes")
                    return
    print("No")


if __name__ == "__main__":
    main()
