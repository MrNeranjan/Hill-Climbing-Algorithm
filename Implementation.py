import random
import sys

# Function to read the input file and parse the delivery_map, number of lorries, and their capacities
def read_input_file(input_filename):
    delivery_map = []
    lorry_capacities = {}
    
    with open(input_filename, 'r') as file:
        lines = file.read().splitlines()

    # Determine the number of lorries and parse lorry information
    num_lorries = 0
    for line in lines:
        if line.startswith("truck_"):
            num_lorries += 1
            lorry_info = line.split('#')
            lorry_name = lorry_info[0]
            lorry_capacity = int(lorry_info[1])
            lorry_capacities[lorry_name] = lorry_capacity
        else:
            # Parse the delivery_map matrix
            row = line.split(',')
            # Handle "N" values by treating them as sys.maxsize
            delivery_map.append([int(length) if length != 'N' else sys.maxsize for length in row])

    return delivery_map, num_lorries, lorry_capacities

# Initialize the solution by distributing deliveries to lorries
def initialize_solution(delivery_map, num_lorries, lorry_capacities):
    num_locations = len(delivery_map)
    delivery_locations = list(range(1, num_locations))  # Exclude the courier service station 'a'
    solution = [[] for _ in range(num_lorries)]

    # Shuffle the list of delivery locations
    random.shuffle(delivery_locations)

    # Assign deliveries to lorries while respecting capacity constraints
    for location in delivery_locations:
        for lorry in solution:
            if len(lorry) < lorry_capacities[f"truck_{solution.index(lorry) + 1}"]:
                lorry.append(location)
                break

    return solution

# Calculate the total length of a solution
def calculate_total_length(solution, delivery_map):
    total_length = 0
    for lorry in solution:
        current_location = 0  # Start at 'a'
        for location in lorry:
            total_length += delivery_map[current_location][location]
            current_location = location

    return total_length

# Perform the Hill Climbing algorithm to optimize the solution
def hill_climbing_for_route_finding(delivery_map, num_lorries, lorry_capacities, max_iterations=1000):
    best_solution = initialize_solution(delivery_map, num_lorries, lorry_capacities)
    best_length = calculate_total_length(best_solution, delivery_map)
    
    # Perform multiple iterations of Hill Climbing
    for i in range(max_iterations):
        # Copy the current solution for modification
        solution_copy = [lorry[:] for lorry in best_solution]
        
        # Select random lorries to swap locations
        lorry_indices = random.sample(range(num_lorries), 2)
        lorry_i, lorry_j = lorry_indices
        
        # Randomly select locations from each lorry
        location_i = random.choice(solution_copy[lorry_i])
        location_j = random.choice(solution_copy[lorry_j])
        
        # Swap locations between the two lorries
        solution_copy[lorry_i].remove(location_i)
        solution_copy[lorry_j].remove(location_j)
        solution_copy[lorry_i].append(location_j)
        solution_copy[lorry_j].append(location_i)
        
        new_length = calculate_total_length(solution_copy, delivery_map)
        
        if new_length < best_length:
            best_solution = solution_copy
            best_length = new_length

    return best_solution, best_length

def main():
    # Read the input file
    input_file = "input.txt"
    delivery_map, num_lorries, lorry_capacities = read_input_file(input_file)
    
    # Run the Hill Climbing algorithm
    num_iterations = 1000 # Number of iterations for the Hill Climbing search
    best_solution = None
    best_length = sys.maxsize
    
    for i in range(num_iterations):
        optimized_solution, total_length = hill_climbing_for_route_finding(delivery_map, num_lorries, lorry_capacities)
        if total_length < best_length:
            best_solution = optimized_solution
            best_length = total_length

    # Write the optimized solution to the output file
    output_file = "output.txt"
    with open(output_file, "w") as file:
        for i, route in enumerate(best_solution):
            lorry_number = i + 1
            # Convert location to letter (a, b, c, ...)
            delivery_sequence = ','.join([chr(97 + location) for location in route if location != 0]) 
            file.write(f"truck_{lorry_number}#{delivery_sequence}\n")
        file.write(str(best_length))

if __name__ == '__main__':
    main()

