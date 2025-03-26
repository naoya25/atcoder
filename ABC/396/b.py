def main():
    q = int(input())
    cards = [0] * 100
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            cards.append(query[1])
        else:
            c = cards.pop()
            print(c)
    return


if __name__ == "__main__":
    main()
