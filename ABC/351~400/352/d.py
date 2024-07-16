from collections import defaultdict, deque
import heapq


def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    dd = defaultdict(int)
    for i in range(n):
        dd[p[i] - 1] = i

    s_arr = list(map(lambda x: dd[x], range(n)))

    min_heap = []
    max_heap = []
    min_deque = deque()
    max_deque = deque()

    for i in range(k):
        heapq.heappush(min_heap, (s_arr[i], i))
        heapq.heappush(max_heap, (-s_arr[i], i))
        while min_deque and min_deque[-1] > s_arr[i]:
            min_deque.pop()
        min_deque.append(s_arr[i])
        while max_deque and max_deque[-1] < s_arr[i]:
            max_deque.pop()
        max_deque.append(s_arr[i])

    ans = float("inf")

    for i in range(n - k + 1):
        while min_heap[0][1] < i:
            heapq.heappop(min_heap)
        while max_heap[0][1] < i:
            heapq.heappop(max_heap)

        current_min = min_heap[0][0]
        current_max = -max_heap[0][0]
        ans = min(ans, current_max - current_min)

        if i + k < n:
            new_elem = s_arr[i + k]
            heapq.heappush(min_heap, (new_elem, i + k))
            heapq.heappush(max_heap, (-new_elem, i + k))
            while min_deque and min_deque[-1] > new_elem:
                min_deque.pop()
            min_deque.append(new_elem)
            while max_deque and max_deque[-1] < new_elem:
                max_deque.pop()
            max_deque.append(new_elem)

    print(ans)


if __name__ == "__main__":
    main()
