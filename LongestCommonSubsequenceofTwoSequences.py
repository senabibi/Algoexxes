def lcs_length(A, B):
    len_A, len_B = len(A), len(B)
    dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]

    for i in range(len_A):
        for j in range(len_B):
            if A[i] == B[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[len_A][len_B]


n = int(input(" "))
A = list(map(int, input(" ").split()))

m = int(input(" "))
B = list(map(int, input(" ").split()))

# Calculate LCS length
print("", lcs_length(A, B))
