import itertools


def main():
    n, m, k = map(int, input().split())

    keys_arr = []  # さすカギの全パターン
    numbers = list(range(n))
    for r in range(n + 1):
        keys_arr += list(itertools.combinations(numbers, r))
    # print(keys_arr)

    not_ans_indexes = set()

    for _ in range(m):
        i_arr = input().split()
        c = int(i_arr[0])
        a = list(map(lambda x: int(x) - 1, i_arr[1:-1]))
        r = i_arr[-1]
        for i in range(2**n):
            keys = keys_arr[i]
            if not judge(k, keys, c, a, r):
                not_ans_indexes.add(i)
    print(2**n - len(not_ans_indexes))
    return


# k:正しい本数, door:答え候補, c:試したカギの本数, a: 試したカギのリスト, r: 正誤判定
def judge(k, door, c, a, r):
    cnt = 0
    for ai in a:
        if ai in door:
            cnt += 1
    if r == "o":
        if cnt >= k:
            return True
        return False
    else:
        if cnt < k:
            return True
        return False


if __name__ == "__main__":
    main()
