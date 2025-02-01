def main():
    n, q = map(int, input().split())
    pigeon_web = {i: i for i in range(n)}
    web_count = {i: 1 for i in range(n)}

    count = 0
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            p = query[1] - 1
            h = query[2] - 1

            web_count[pigeon_web[p]] -= 1
            web_count[h] += 1

            if web_count[pigeon_web[p]] == 1:
                count -= 1
            if web_count[h] == 2:
                count += 1

            pigeon_web[p] = h

        elif query[0] == 2:
            print(count)

    return


if __name__ == "__main__":
    main()
