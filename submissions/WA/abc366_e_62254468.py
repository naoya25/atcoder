# URL: https://atcoder.jp/contests/abc366/submissions/62254468
# id: 62254468
# epoch_second: 1738406028
# problem_id: abc366_e
# contest_id: abc366
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 3015
# result: WA
# execution_time: 261


# submitted code
def count_valid_points(N, D, points):
    # x座標とy座標を別々にリストに格納
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    
    # x座標とy座標をソート
    x_coords.sort()
    y_coords.sort()
    
    # 累積和を計算
    x_prefix = [0] * (N + 1)
    y_prefix = [0] * (N + 1)
    for i in range(N):
        x_prefix[i + 1] = x_prefix[i] + x_coords[i]
        y_prefix[i + 1] = y_prefix[i] + y_coords[i]
    
    # 条件を満たす (x, y) の個数をカウント
    count = 0
    
    # x座標の範囲を探索
    # 中央値から D の範囲内で探索
    median_x = x_coords[N // 2]
    median_y = y_coords[N // 2]
    
    # x座標の範囲を決定
    x_min = median_x - D
    x_max = median_x + D
    
    # y座標の範囲を決定
    y_min = median_y - D
    y_max = median_y + D
    
    # x座標の範囲を全探索
    for x in range(x_min, x_max + 1):
        # x座標に対するマンハッタン距離の総和を計算
        # 二分探索で x 以下の最大のインデックスを求める
        left = 0
        right = N
        while left < right:
            mid = (left + right) // 2
            if x_coords[mid] <= x:
                left = mid + 1
            else:
                right = mid
        idx = left
        
        # 累積和を利用して総和を計算
        sum_x = x * idx - x_prefix[idx] + (x_prefix[N] - x_prefix[idx]) - x * (N - idx)
        
        # y座標の範囲を決定
        # D - sum_x が y座標の差の総和の上限
        remaining_D = D - sum_x
        if remaining_D < 0:
            continue
        
        # y座標の範囲を計算
        y_lower = median_y - remaining_D
        y_upper = median_y + remaining_D
        
        # y座標の範囲内で条件を満たす y の個数を計算
        # 二分探索で y_lower 以上の最小のインデックスを求める
        left_y = 0
        right_y = N
        while left_y < right_y:
            mid_y = (left_y + right_y) // 2
            if y_coords[mid_y] < y_lower:
                left_y = mid_y + 1
            else:
                right_y = mid_y
        lower_idx = left_y
        
        # 二分探索で y_upper 以下の最大のインデックスを求める
        left_y = 0
        right_y = N
        while left_y < right_y:
            mid_y = (left_y + right_y) // 2
            if y_coords[mid_y] <= y_upper:
                left_y = mid_y + 1
            else:
                right_y = mid_y
        upper_idx = left_y
        
        # y座標の範囲内の点の個数を加算
        count += upper_idx - lower_idx
    
    return count

# 入力例
N, D = map(int, input().split())
points = []
for _ in range(N):
  dd = tuple(map(int, input().split()))
  points.append(dd)

# 結果を出力
print(count_valid_points(N, D, points))  # 出力: 21