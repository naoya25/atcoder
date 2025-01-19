import itertools


# make10
# 4つの数字が与えられた時に、10になる式のパターンを求める
def calc_patterns(ns_arr):
    patterns = []
    # 数字の並び替え
    for a, b, c, d in itertools.permutations(ns_arr):
        # 演算のパターン
        for o1, o2, o3 in list(itertools.product(("+", "-", "*", "/"), repeat=3)):
            # 括弧のパターン
            expressions = [
                f"{a} {o1} {b} {o2} {c} {o3} {d}",
                f"({a} {o1} {b}) {o2} {c} {o3} {d}",
                f"{a} {o1} ({b} {o2} {c}) {o3} {d}",
                f"{a} {o1} {b} {o2} ({c} {o3} {d})",
                f"({a} {o1} {b} {o2} {c}) {o3} {d}",
                f"{a} {o1} ({b} {o2} {c} {o3} {d})",
                f"({a} {o1} {b}) {o2} ({c} {o3} {d})",
                f"(({a} {o1} {b}) {o2} {c}) {o3} {d}",
                f"({a} {o1} ({b} {o2} {c})) {o3} {d}",
                f"{a} {o1} (({b} {o2} {c}) {o3} {d})",
                f"{a} {o1} ({b} {o2} ({c} {o3} {d}))",
            ]
            for expression in expressions:
                try:
                    if eval(expression) == 10:
                        patterns.append(expression)
                except ZeroDivisionError:
                    pass
    return patterns


def main():
    # ns_arr = map(int, input().split())
    # patterns = calc_patterns(ns_arr)
    # for pattern in patterns:
    #     print(pattern)
    # return

    patterns = {}
    for ns_array in itertools.combinations(range(1, 10), 4):
        patterns[ns_array] = len(calc_patterns(ns_array))

    print(patterns)


if __name__ == "__main__":
    main()
