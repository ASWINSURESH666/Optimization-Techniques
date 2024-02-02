'''(5) A bakery sells two types of cakes, chocolate and vanilla. The bakery has a daily budget of 500 dollars and can produce at most 400 cakes per day.
  Each chocolate cake costs 2 dollars to make and sells for 5 dollars, while each vanilla cake costs 1 dollar to make and sells for 3 dollars.
  The bakery also has to satisfy the demand of at least 100 chocolate cakes and at least 50 vanilla cakes per day.
  How many cakes of each type should the bakery make to maximize its revenue?
  What is the maximum revenue?
  Implement using linear programming package '''

from scipy.optimize import linprog

c = [-5, -3]


A = [[-2, -1], [-5, -3]]


b = [-100, -50]


x0_bounds = (0, None)
x1_bounds = (0, None)


A_eq = [[2, 1]]
b_eq = [500]
A_ub = [[1, 1]]
b_ub = [400]


result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=[x0_bounds, x1_bounds], method='highs')

optimal_chocolate_cakes = result.x[0]
optimal_vanilla_cakes = result.x[1]
max_revenue = -result.fun

print(f"Optimal number of chocolate cakes: {optimal_chocolate_cakes}")
print(f"Optimal number of vanilla cakes: {optimal_vanilla_cakes}")
print(f"Maximum revenue: ${max_revenue}")
