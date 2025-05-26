# URL: https://atcoder.jp/contests/abc407/submissions/66123918
# id: 66123918
# epoch_second: 1748092098
# problem_id: abc407_e
# contest_id: abc407
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 450.0
# length: 572
# result: AC
# execution_time: 507


# submitted code
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
