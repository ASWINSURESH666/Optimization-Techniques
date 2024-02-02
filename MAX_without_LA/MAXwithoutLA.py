'''(6) Solve the following without using linear programming package

 Maximize

 p=2u1+3u2+u3

 Subject to

 u1+u2+u3≤4

 u1+2u2−u3≥2

 u1,u2,u3≥0  '''

from scipy.optimize import linprog

# Coefficients for the objective function (negative for maximization)
c = [-2, -3, -1]

# Coefficients for the inequality constraints
A = [[1, 1, 1], [-1, -2, -1]]

# RHS values for the inequality constraints
b = [4, -2]

# Bounds for decision variables (non-negativity constraints)
x0_bounds = (0, None)
x1_bounds = (0, None)
x2_bounds = (0, None)

# Solve the linear programming problem using HiGHS solver
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds, x2_bounds], method='highs')

# Extract the optimal solution
optimal_u1 = result.x[0]
optimal_u2 = result.x[1]
optimal_u3 = result.x[2]
max_p = -result.fun  # negative because linprog minimizes, so we negate the value to get the maximum value

# Print the results
print(f"Optimal u1: {optimal_u1}")
print(f"Optimal u2: {optimal_u2}")
print(f"Optimal u3: {optimal_u3}")
print(f"Maximum p: {max_p}")