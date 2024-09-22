def max_gold(capacity, weights):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                val = dp[i - 1][w - weights[i - 1]] + weights[i - 1]
                if dp[i][w] < val:
                    dp[i][w] = val

    return dp[n][capacity]


W, n = map(int, input(" ").split())
weights = list(map(int, input(" ").split()))

print(" ", max_gold(W, weights))
