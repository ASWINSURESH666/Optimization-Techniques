import numpy as np
from scipy.optimize import linear_sum_assignment

def solve_assignment(cost_matrix):
    # Convert the cost matrix to a numpy array
    cost_matrix = np.array(cost_matrix)
    
    # Use the Hungarian Algorithm to find the optimal assignment
    row_indices, col_indices = linear_sum_assignment(cost_matrix)
    
    # Create an assignment matrix
    assignment_matrix = np.zeros_like(cost_matrix, dtype=bool)
    assignment_matrix[row_indices, col_indices] = True
    
    # Calculate the total cost
    total_cost = cost_matrix[assignment_matrix].sum()
    
    # Return the assignment matrix and total cost
    return assignment_matrix, total_cost

# Example usage:
cost_matrix = [
    [9, 11, 14, 11, 7],
    [6, 15, 13, 13, 10],
    [12, 13, 6, 8, 8],
    [11, 9, 10, 12, 9],
    [7, 12, 14, 10, 14]
]

assignment_matrix, total_cost = solve_assignment(cost_matrix)

# Output the results
print("Optimal Assignment Matrix:")
print(assignment_matrix)
print("Total Assignment Cost:", total_cost)
