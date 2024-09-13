def primitive_calculator(n):
    minOperations = [0] * (n + 1)
    for i in range(2, n + 1):
        min_ops = minOperations[i - 1] + 1
        if i % 2 == 0:
            min_ops = min(min_ops, minOperations[i // 2] + 1)
        if i % 3 == 0:
            min_ops = min(min_ops, minOperations[i // 3] + 1)
        minOperations[i] = min_ops

    # Backtracking the sequence
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0 and minOperations[n] - 1 == minOperations[n // 3]:
            n = n // 3
        elif n % 2 == 0 and minOperations[n] - 1 == minOperations[n // 2]:
            n = n // 2
        else:
            n = n - 1
    sequence.reverse()

    return minOperations[-1], sequence

# Example
n = int(input(" "))  # Convert input to integer
min_ops, seq = primitive_calculator(n)
print(" ", min_ops)
print(" ", seq)
