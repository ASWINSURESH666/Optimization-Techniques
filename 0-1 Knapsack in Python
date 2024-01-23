def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    max_value = dp[n][capacity]

    included_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            included_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    included_items.reverse()

    return max_value, included_items

# User input
n = int(input("Enter the number of items: "))
values = [int(input(f"Enter value for item {i + 1}: ")) for i in range(n)]
weights = [int(input(f"Enter weight for item {i + 1}: ")) for i in range(n)]
capacity = int(input("Enter the capacity of the knapsack: "))

# Run the knapsack algorithm
max_value, included_items = knapsack_01(values, weights, capacity)

# Display the result
print(f"Maximum value: {max_value}")
print(f"Included items: {included_items}")
