import numpy as np

def nearest_neighbor_tsp(distances):
    num_cities = len(distances)
    unvisited_cities = set(range(num_cities))
    current_city = 0
    tour = [current_city]
    unvisited_cities.remove(current_city)
    
    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: distances[current_city][city])
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city
    
    # Return to the starting city
    tour.append(tour[0])
    
    # Calculate the total distance of the tour
    total_distance = sum(distances[tour[i]][tour[i+1]] for i in range(num_cities))
    
    return tour, total_distance

# Example usage:
# Define the distances between cities (replace with your own data)
distances = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

# Find the shortest route
shortest_route, total_distance = nearest_neighbor_tsp(distances)

# Output the results
print("Shortest Route:", shortest_route)
print("Total Distance:", total_distance)
