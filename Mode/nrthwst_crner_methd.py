def northwest_corner_method(cost_matrix, supply, demand):
    num_rows = len(supply)
    num_cols = len(demand)
    allocation = [[0] * num_cols for _ in range(num_rows)]
    total_cost = 0

    row = 0
    col = 0

    while row < num_rows and col < num_cols:
        # Allocate as much as possible from current cell
        allocation[row][col] = min(supply[row], demand[col])

        # Update supply and demand
        supply[row] -= allocation[row][col]
        demand[col] -= allocation[row][col]

        # Move to the next cell
        if supply[row] == 0:
            row += 1
        else:
            col += 1

    # Calculate total cost
    for i in range(num_rows):
        for j in range(num_cols):
            total_cost += allocation[i][j] * cost_matrix[i][j]

    return allocation, total_cost

# Example usage:
cost_matrix = [
    [3, 1, 7, 4],
    [2, 6, 5, 9],
    [8, 3, 3, 2]
]

supply = [300, 400, 500]
demand = [250, 350, 400, 200]

allocation, total_cost = northwest_corner_method(cost_matrix, supply, demand)
print("Allocation Matrix:")
for row in allocation:
    print(row)
print("Total Cost:", total_cost)
