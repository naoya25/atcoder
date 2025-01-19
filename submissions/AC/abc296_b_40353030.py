# URL: https://atcoder.jp/contests/abc296/submissions/40353030
# Language: Python (3.8.2)

# submitted code
string = "abcdefgh"
s_list = [list(input()) for _ in range(8)]
s_list = sum(s_list, [])
s_in = s_list.index("*")
print(string[s_in % 8] + str(8 - (s_in // 8)))