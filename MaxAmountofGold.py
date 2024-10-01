def optimal_weight(W, w):
    # Initialize the DP table
    K = [[0 for _ in range(W + 1)] for _ in range(len(w) + 1)]
    
    # Build table K[][] in bottom-up manner
    for i in range(len(w) + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif w[i - 1] <= j:
                K[i][j] = max(K[i - 1][j], w[i - 1] + K[i - 1][j - w[i - 1]])
            else:
                K[i][j] = K[i - 1][j]
                
    return K[len(w)][W]

if __name__ == "__main__":
    W, n = map(int, input().split())
    w = list(map(int, input().split()))
    
    # Sorting the weights in reverse order (largest to smallest)
    w.sort(reverse=True)
    
    print(optimal_weight(W, w))
