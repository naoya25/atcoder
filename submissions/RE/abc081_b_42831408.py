# URL: https://atcoder.jp/contests/abc081/submissions/42831408
# Language: Python (3.8.2)

# submitted code
n = int(input())
numbers = list(map(int, input().split()))
count = 0

def isEven():
    return all([num % 2 == 0 for num in numbers])

while isEven():
    numbers=[num / 2 for num in numbers]
    count += 1

print(counter)