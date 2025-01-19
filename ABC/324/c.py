import sys


input = lambda: sys.stdin.readline().rstrip()


def judge(a, b):
    if len(a) == len(b) - 1:
        return False
    i = 0
    for j in range(len(b)):
        while i < len(a) and a[i] != b[j]:
            i += 1
        if i == len(a):
            return False
        i += 1
    return True


def main():
    n, t_ = input().split()
    n = int(n)

    ans = []
    for i in range(n):
        s = input().strip()

        if s == t_:
            ans.append(i + 1)
            continue

        if len(s) == len(t_):
            cnt = 0
            for a, b in zip(s, t_):
                if a != b:
                    cnt += 1
                if cnt > 1:
                    break
            else:
                ans.append(i + 1)
        elif len(s) - len(t_) == 1:
            if judge(s, t_):
                ans.append(i + 1)
        elif len(t_) - len(s) == 1:
            if judge(t_, s):
                ans.append(i + 1)

    print(len(ans))
    if len(ans) > 0:
        print(*ans)


if __name__ == "__main__":
    main()
    # python main.py < input.txt
