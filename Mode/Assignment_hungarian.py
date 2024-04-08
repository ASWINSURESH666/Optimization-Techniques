import numpy as np
from scipy.optimize import linear_sum_assignment

def hungarian_algorithm(cost_matrix):
    # Input validation
    if not isinstance(cost_matrix, np.ndarray):
        raise ValueError("Input cost matrix must be a numpy array")
    if cost_matrix.ndim != 2 or cost_matrix.shape[0] != cost_matrix.shape[1]:
        raise ValueError("Input cost matrix must be square")
    if cost_matrix.size == 0:
        raise ValueError("Input cost matrix cannot be empty")

    # Step 1: Reduce the cost matrix
    print("Cost Matrix:")
    print(cost_matrix)
    
    reduced_matrix = cost_matrix - np.min(cost_matrix, axis=0)
    reduced_matrix -= np.min(reduced_matrix, axis=1)[:, np.newaxis]
    
    print("Reduced Matrix:")
    print(reduced_matrix)
    
    # Steps 2-7: Hungarian algorithm
    while True:
        # Step 2: Find the minimum number of lines
        num_lines = np.sum(reduced_matrix == 0)
        print("Number of Lines:", num_lines)
        
        # Step 3: Cover all zeroes with the minimum number of lines
        if num_lines == len(cost_matrix):
            break
        
        row_covered = np.zeros(len(cost_matrix), dtype=bool)
        col_covered = np.zeros(len(cost_matrix), dtype=bool)
        zero_positions = np.argwhere(reduced_matrix == 0)
        
        for i, j in zero_positions:
            if not row_covered[i] and not col_covered[j]:
                row_covered[i] = True
                col_covered[j] = True
        
        # Step 4: Test for optimality
        if np.sum(row_covered) + np.sum(col_covered) == len(cost_matrix):
            break
        
        # Step 5: Modify the cost matrix
        min_uncovered_value = np.min(reduced_matrix[~row_covered][:, ~col_covered], initial=int(1e9))
        reduced_matrix[~row_covered] -= min_uncovered_value
        reduced_matrix[:, col_covered] += min_uncovered_value
    
    # Step 7: Assign tasks to workers
    row_indices, col_indices = linear_sum_assignment(reduced_matrix)
    assignment = np.zeros_like(cost_matrix)
    assignment[row_indices, col_indices] = 1
    
    return assignment

# Example usage with your provided cost matrix
cost_matrix = np.array([[9, 11, 14, 11, 7],
                        [6, 15, 13, 13, 10],
                        [12, 13, 6, 8, 8],
                        [11, 9, 10, 12, 9],
                        [7, 12, 14, 10, 14]])

try:
    optimal_assignment = hungarian_algorithm(cost_matrix)
    print("Optimal Assignment:")
    print(optimal_assignment)
except ValueError as e:
    print("Error:", e)
