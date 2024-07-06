from collections import deque


def main():
    n = int(input())
    s = list(input() + "..")
    t = list(input() + "..")

    if not (s.count("W") == t.count("W") and s.count("B") == t.count("B")):
        print(-1)
        return

    # 全探索しようBFS
    # 現在の並び順, カウント
    queue = deque([(s, 0)])
    already_s = set()
    already_s.add("".join(s))

    ans = float("inf")
    while queue:
        si, count = queue.popleft()
        if si == t:
            ans = min(ans, count)
            continue

        """やること
        - 空の位置探す
        - 石が2個並んでる位置を探す(全パターン)
        並び替えてqueueに打ち込む
        """
        empty_x = -1
        possible_arr = []
        for i in range(n + 1):
            if si[i] == "." and empty_x == -1:
                empty_x = i
                continue
            if si[i] != "." and si[i + 1] != ".":
                possible_arr.append(i)

        for i in possible_arr:
            new_s = si.copy()
            new_s[empty_x] = new_s[i]
            new_s[empty_x + 1] = new_s[i + 1]
            new_s[i], new_s[i + 1] = ".", "."
            if "".join(new_s) not in already_s:
                queue.append((new_s, count + 1))
                already_s.add("".join(new_s))

    print(ans if ans != float("inf") else -1)

    return


if __name__ == "__main__":
    main()
