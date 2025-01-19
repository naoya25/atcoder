import itertools


def main():
    """メモ
    とりあえず2つにさえ分ければでかい順に並べればいける
    2つに分ける方法
    n <= 10^9 →文字列としたら9文字の文字列のグループ分け
    """
    n_str = input()
    ans = 0

    combinations = []
    for r in range(1, len(n_str)):
        combinations.extend(itertools.combinations(n_str, r))

    for combo in combinations:
        a = sorted(combo, key=int, reverse=True)
        b = sorted(n_str, key=int, reverse=True)
        for char in combo:
            b.remove(char)

        if a[0] == "0" or b[0] == "0":
            continue
        v = int("".join(a)) * int("".join(b))
        ans = max(ans, v)
    print(ans)

    return


if __name__ == "__main__":
    main()
