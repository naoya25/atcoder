# URL: https://atcoder.jp/contests/abc366/submissions/62254539
# id: 62254539
# epoch_second: 1738406248
# problem_id: abc366_e
# contest_id: abc366
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 1807
# result: TLE
# execution_time: 2211


# submitted code
import bisect


def count_valid_points(N, D, points):
    # 分离 x 和 y 坐标
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]

    # 对 x 和 y 坐标进行排序
    x_coords.sort()
    y_coords.sort()

    # 计算 x 和 y 的中位数
    median_x = x_coords[N // 2]
    median_y = y_coords[N // 2]

    # 计算 x 和 y 的累积和
    x_prefix = [0] * (N + 1)
    y_prefix = [0] * (N + 1)

    for i in range(N):
        x_prefix[i + 1] = x_prefix[i] + x_coords[i]
        y_prefix[i + 1] = y_prefix[i] + y_coords[i]

    # 计算满足条件的 (x, y) 的个数
    count = 0

    # 枚举 x 的范围
    for x in range(median_x - D, median_x + D + 1):
        # 计算 x 的贡献
        idx = bisect.bisect_left(x_coords, x)
        x_sum = x * idx - x_prefix[idx] + (x_prefix[N] - x_prefix[idx]) - x * (N - idx)

        # 如果 x 的贡献已经大于 D，跳过
        if x_sum > D:
            continue

        # 计算 y 的最大允许贡献
        max_y_sum = D - x_sum

        # 枚举 y 的范围
        for y in range(median_y - max_y_sum, median_y + max_y_sum + 1):
            # 计算 y 的贡献
            idy = bisect.bisect_left(y_coords, y)
            y_sum = (
                y * idy - y_prefix[idy] + (y_prefix[N] - y_prefix[idy]) - y * (N - idy)
            )

            # 如果 y 的贡献满足条件，增加计数
            if y_sum <= max_y_sum:
                count += 1

    return count


# 示例输入
N, D = map(int, input().split())
points = []
for _ in range(N):
    dd = tuple(map(int, input().split()))
    points.append(dd)

# 计算满足条件的点的个数
result = count_valid_points(N, D, points)
print(result)  # 输出: 6
