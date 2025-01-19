"""
sort sorted の違い
"""

arr = [3, 5, 1, 4, 9, 6, 3]

arr1 = sorted(arr)  # sorted関数を使った
arr.sort()  # sortメソッド

print(arr1)
print(arr)
