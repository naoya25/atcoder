# URL: https://atcoder.jp/contests/abs/submissions/30556568
# Language: Python (3.8.2)

# submitted code
s = str(input())[::-1]
words = ['dream'[::-1], 'dreamer'[::-1], 'erase'[::-1], 'eraser'[::-1]]
while len(s) != 0:
    Exist = False
    for word in words:
        if s[:len(word)] == word:
            s = s[len(word):]
            Exist = True
            break
    if Exist == False:
        print('NO')
        break
    elif s == '':
        print('YES')
        break