def lcs_length_of_three(A, B, C):
    len_A, len_B, len_C = len(A), len(B), len(C)
    dp = [[[0 for _ in range(len_C + 1)] for _ in range(len_B + 1)] for _ in range(len_A + 1)]

    for i in range(1, len_A + 1):
        for j in range(1, len_B + 1):
            for k in range(1, len_C + 1):
                if A[i - 1] == B[j - 1] == C[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[len_A][len_B][len_C]

# Read input from user
n = int(input(" "))
A = list(map(int, input(" ").split()))

m = int(input(" "))
B = list(map(int, input(" ").split()))

l = int(input(" "))
C = list(map(int, input(" ").split()))

# Calculate LCS length
print(" ", lcs_length_of_three(A, B, C))
