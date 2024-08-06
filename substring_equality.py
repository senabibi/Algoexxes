class Solver:
    def __init__(self, s):
        self.s = s

    def ask(self, a, b, l):
        return self.s[a:a+l] == self.s[b:b+l]

def main():
    s = input().rstrip()
    q = int(input())
    solver = Solver(s)
    for _ in range(q):
        a, b, l = map(int, input().split())
        print("Yes" if solver.ask(a, b, l) else "No")

if __name__ == '__main__':
    main()
