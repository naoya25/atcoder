n = int(input())
nums = sorted(list(map(int, input().split())), reverse=True)

if n > 1:
  a_point = sum(nums[::2])
  b_point = sum(nums[1::2])
  print(a_point - b_point)
else:
  print(nums[0])
