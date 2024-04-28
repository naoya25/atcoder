n = int(input())
cards = list(map(int, input().split()))

cards.sort(reverse=True)
# print(cards)
alice_point = 0
bob_point = 0

for i in range(n):
    if i % 2 == 0:
        alice_point += cards[i]
    else:
        bob_point += cards[i]
print(alice_point - bob_point)


# 別解
# n = int(input())
# nums = sorted(list(map(int, input().split())), reverse=True)

# if n > 1:
#   a_point = sum(nums[::2])
#   b_point = sum(nums[1::2])
#   print(a_point - b_point)
# else:
#   print(nums[0])
