n_str = input()
n_sum = 0
for s in n_str:
    n_sum += int(s)
print("Yes" if n_sum % 9 == 0 else "No")
