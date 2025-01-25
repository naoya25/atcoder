from collections import deque


def main():
    n = int(input())
    correct_deck = list(map(int, input().split()))
    if correct_deck == list(range(n)):
        print(0)
        return
    s = int(input())
    shuffles = [tuple(map(int, input().split())) for _ in range(s)]

    deck = list(range(n))

    queue = deque([(deck, 0)])  # 現在の山札、シャッフルした回数
    deck_his = [deck]

    ans = -1
    while queue:  # bfs
        now_deck, count = queue.popleft()

        if now_deck == correct_deck:
            ans = count
            break

        for st in shuffles:
            new_deck = shuffle(now_deck, st)
            if new_deck not in deck_his:
                queue.append((new_deck, count + 1))
                deck_his.append(new_deck)

    print(ans)


def shuffle(now_deck, shuffle_type):
    shuffled_deck = [now_deck[num] for num in shuffle_type]
    return shuffled_deck


if __name__ == "__main__":
    main()
