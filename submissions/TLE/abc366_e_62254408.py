# URL: https://atcoder.jp/contests/abc366/submissions/62254408
# id: 62254408
# epoch_second: 1738405845
# problem_id: abc366_e
# contest_id: abc366
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 1306
# result: TLE
# execution_time: 2214


# submitted code
def count_valid_points(N, D, points):
    # x座標とy座標を別々にリストに格納
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    
    # x座標とy座標をソート
    x_coords.sort()
    y_coords.sort()
    
    # x座標の中央値
    median_x = x_coords[N // 2]
    # y座標の中央値
    median_y = y_coords[N // 2]
    
    # 条件を満たす (x, y) の個数をカウント
    count = 0
    
    # x座標の範囲を探索
    for x in range(median_x - D, median_x + D + 1):
        # y座標の範囲を探索
        for y in range(median_y - D, median_y + D + 1):
            # マンハッタン距離の総和を計算
            total_distance = 0
            for i in range(N):
                total_distance += abs(x - x_coords[i]) + abs(y - y_coords[i])
                if total_distance > D:
                    break
            # 条件を満たす場合、カウントを増やす
            if total_distance <= D:
                count += 1
    
    return count

# 入力例
N, D = map(int, input().split())
points = []
for _ in range(N):
  dd = tuple(map(int, input().split()))
  points.append(dd)

# 結果を出力
print(count_valid_points(N, D, points))  # 出力: 21