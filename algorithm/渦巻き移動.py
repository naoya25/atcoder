def spiral(center, n):
    x, y = center
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 右、上、左、下
    current_direction = 0  # 移動方向

    coordinates = [(x, y)]

    for step in range(1, n):
        for _ in range(2):  # 移動距離は、1,1,2,2,3,3,4,4,5,5,6,6,7,7,,,, 2個ずつセットなので
            dx, dy = directions[current_direction]
            for _ in range(step):
                x += dx
                y += dy
                coordinates.append((x, y))

            current_direction = (current_direction + 1) % 4

    return coordinates


if __name__ == "__main__":
    result = spiral((0, 0), 10)  # 中心座標、回転数
    print(result)
