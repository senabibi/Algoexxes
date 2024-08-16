def hamming_distance(str1, str2):
    """Calculate the Hamming distance between two strings."""
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))

def solve(k, text, pattern):
    ans = []
    pattern_length = len(pattern)
    for i in range(len(text) - pattern_length + 1):
        if hamming_distance(text[i:i + pattern_length], pattern) <= k:
            ans.append(i)
    return ans

def main():
    while True:
        try:
            k, text, pattern = input().split()
            ans = solve(int(k), text, pattern)
            print(len(ans), *ans)
        except EOFError:
            break

if __name__ == '__main__':
    main()
