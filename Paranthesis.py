def min_and_max(i, j, min_dp, max_dp, operators, digits):
    minimum = float('inf')
    maximum = float('-inf')

    for k in range(i, j):
        a = eval(f"{max_dp[i][k]} {operators[k]} {max_dp[k + 1][j]}")
        b = eval(f"{max_dp[i][k]} {operators[k]} {min_dp[k + 1][j]}")
        c = eval(f"{min_dp[i][k]} {operators[k]} {max_dp[k + 1][j]}")
        d = eval(f"{min_dp[i][k]} {operators[k]} {min_dp[k + 1][j]}")

        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)

    return minimum, maximum

def max_value(expression):
    digits = [int(d) for d in expression if d.isdigit()]
    operators = [op for op in expression if not op.isdigit()]

    n = len(digits)
    min_dp = [[0 for _ in range(n)] for _ in range(n)]
    max_dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        min_dp[i][i] = digits[i]
        max_dp[i][i] = digits[i]

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            min_dp[i][j], max_dp[i][j] = min_and_max(i, j, min_dp, max_dp, operators, digits)

    return max_dp[0][n - 1]

# Example usage
expression = input(" ")
print("", max_value(expression))
