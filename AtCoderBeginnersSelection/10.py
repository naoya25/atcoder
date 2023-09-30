# s = input().replace('eraser', '').replace('erase', '').replace('dreamer', '').replace('dream', '')
# print('YES' if s == '' else 'NO')

import re
s = input()
if re.compile(r'^(?:dream(?:er)?|eraser?)+$').search(s):
  print('YES')
else:
  print('NO')
