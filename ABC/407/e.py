import heapq


def calc(n, a):
    total = sum(a)
    removed_sum = 0
    heap = []

    for i, val in enumerate(a, 1):
        heapq.heappush(heap, -val)
        removed_sum += val

        if len(heap) > (i // 2):
            largest = -heapq.heappop(heap)
            removed_sum -= largest

    return total - removed_sum


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(input()) for _ in range(2 * n)]
        ans = calc(n, a)
        print(ans)


if __name__ == "__main__":
    main()
