def main():
    n = int(input())
    events = []
    for _ in range(n):
        l, r = map(int, input().split())
        events.append((l, 'start'))
        events.append((r, 'end'))

    events.sort(key=lambda x: (x[0], x[1] == 'end'))

    current_intervals = 0
    ans = 0
    for event in events:
        if event[1] == 'start':
            ans += current_intervals
            current_intervals += 1
        else:
            current_intervals -= 1

    print(ans)
    return

if __name__ == "__main__":
    main()
