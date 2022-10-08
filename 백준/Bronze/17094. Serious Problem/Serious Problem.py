import sys
input = sys.stdin.readline

s_len = int(input())
s = input()

print('2' if s.count('2') > s.count('e') else ('e' if s.count('e') > s.count('2') else 'yee'))