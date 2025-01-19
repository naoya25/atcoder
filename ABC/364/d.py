import bisect
import heapq


def find_distance(A, B, k):
    index = bisect.bisect_left(A, B)
    distances = []

    for i in range(max(0, index - k), min(len(A), index + k)):
        heapq.heappush(distances, -abs(A[i] - B))
        if len(distances) > k:
            heapq.heappop(distances)

    return -distances[0]


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for _ in range(q):
        b, k = map(int, input().split())
        d = find_distance(a, b, k)
        print(d)

    return


if __name__ == "__main__":
    main()


# import bisect


# def main():
#     n, q = map(int, input().split())
#     a = sorted(map(int, input().split()))

#     results = []
#     for _ in range(q):
#         b, k = map(int, input().split())

#         left, right = 0, 2 * 10**9
#         while left < right:
#             mid = (left + right) // 2
#             count = bisect.bisect_right(a, b + mid) - bisect.bisect_left(a, b - mid)
#             if count >= k:
#                 right = mid
#             else:
#                 left = mid + 1

#         results.append(left)

#     for result in results:
#         print(result)


# if __name__ == "__main__":
#     main()
