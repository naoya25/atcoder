def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    sorted_a = sorted(a)
    now_vote = sum(a)

    print(a)
    print(sorted_a)

    for ai in a:
        if ai < sorted_a[-m]:  # 現在当選しない人
            necessary_vote = sorted_a[-m] + 1 - ai # 当選するために必要な票
            print(sorted_a[-m], ai)

    return


if __name__ == "__main__":
    main()
