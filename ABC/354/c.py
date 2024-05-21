def main():
    n = int(input())
    cards = [[i + 1] + list(map(int, input().split())) for i in range(n)]
    cards.sort(key=lambda x: x[1], reverse=True)
    # print(cards)

    i, pa, pc = cards[0]
    ans = [i]
    for i, a, c in cards[1:]:
        if pc >= c:
            ans.append(i)
            pa, pc = a, c
    print(len(ans))
    ans.sort()
    print(*ans)
    return


if __name__ == "__main__":
    main()
