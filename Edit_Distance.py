def edit_distance(str1, str2):
    len_str1, len_str2 = len(str1), len(str2)
    dp = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]

    for i in range(len_str1 + 1):
        for j in range(len_str2 + 1):
            if i == 0:
                dp[i][j] = j  # Filling the first row with the index of str2
            elif j == 0:
                dp[i][j] = i  # Filling the first column with the index of str1
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # Characters match, no operation needed
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],    # Insert
                                   dp[i][j - 1],    # Remove
                                   dp[i - 1][j - 1]) # Replace

    return dp[len_str1][len_str2]

# User input
str1 = input(" ")
str2 = input(" ")

# Calculate and print the edit distance
print(" ", edit_distance(str1, str2))
