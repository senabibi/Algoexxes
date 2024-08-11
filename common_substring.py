import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

def solve(s, t):
    ans = Answer(0, 0, 0)
    for i in range(len(s)):
        for j in range(len(t)):
            for l in range(min(len(s) - i, len(t) - j) + 1):
                if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
                    ans = Answer(i, j, l)
    return ans

def main():
    while True:
        try:
            s, t = input().split()
            ans = solve(s, t)
            print(ans.i, ans.j, ans.len)
        except EOFError:
            break

if __name__ == '__main__':
    main()
