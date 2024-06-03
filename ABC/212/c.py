import bisect


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()

    ans = float("inf")
    for ai in a:
        bi = find_closest_element(b, ai)
        ans = min(ans, abs(ai - bi))
    print(ans)
    return


def find_closest_element(arr, target):
    # 挿入すべき位置を見つける
    pos = bisect.bisect_left(arr, target)

    # リストの範囲外をチェック
    if pos == 0:
        return arr[0]
    if pos == len(arr):
        return arr[-1]

    # 直前と直後の値を比較して近い方を返す
    before = arr[pos - 1]
    after = arr[pos]
    if after - target < target - before:
        return after
    else:
        return before


if __name__ == "__main__":
    main()
