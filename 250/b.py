n, a, b = map(int, input().split())

def create_row(s1, s2):
    row = ''
    for c in range(n):
        if c % 2 == 0:
            row += s1 * b
        else:
            row += s2 * b
    return row


for r in range(n * a):
    if r // a % 2 == 0:
        print(create_row('.', '#'))
    else:
        print(create_row('#', '.'))
