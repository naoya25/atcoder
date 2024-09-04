# AtCoder 競プロ典型 90 問 解くぞ!!

https://atcoder.jp/contests/typical90/tasks

# 学びメモ

- 1
  - 「最小値の最大化」には二分探索が有効
- 2
  - 2 つの状態しかないもの(今回はカッコ)の時は bit に着目すると良い場合がある
  - O(2\*\*n)が耐えてたら bit 全探索が有効の場合が多い
    - python での bit 全探索は `itertools.product` と `1 << n`の 2 パターンある
    - itertools は辞書順, 1 << n は bit 列順になる
