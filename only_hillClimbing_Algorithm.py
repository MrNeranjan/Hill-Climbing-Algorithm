import random

def random_solution (city_map):
    locations = list(range(len(city_map)))
    solution = []
    
    for i in range(len(city_map)):
        random_location = locations[random.randint(0,len(locations)-1)]
        solution.append(random_location)
        locations.remove(random_location)
    return solution


def calculate_route_length(solution, city_map):
    route_length = 0
    for i in range(len(solution)):
        route_length += city_map[solution[i-1]][solution[i]]
    return route_length

def get_neibours(solution):
    neibours = []
    for i in range(len(solution)):
        for j in range(i+1, len(solution)):
            neibour = solution.copy()
            neibour[i] = solution[j]
            neibour[j] = solution[i]
            neibours.append(neibour)
    return neibours

def get_best_neibour(neibours, city_map):
    best_neibour_route_length = calculate_route_length(neibours[0], city_map)
    best_neibour = neibours[0]
    
    for neibour in neibours:
        neibour_route_length = calculate_route_length(neibour, city_map)
        if neibour_route_length < best_neibour_route_length:
            best_neibour = neibour
            best_neibour_route_length = neibour_route_length
    return best_neibour, best_neibour_route_length

def hillclimbing(city_map):
    current_solution = random_solution(city_map)
    current_route_length = calculate_route_length(current_solution, city_map)
    neibours = get_neibours(current_solution)
    best_neibour, best_neibour_route_length = get_best_neibour(neibours, city_map)
    
    while best_neibour_route_length < current_route_length:
        current_solution = best_neibour
        current_route_length = best_neibour_route_length
        neibours = get_neibours(current_solution)
        best_neibour, best_neibour_route_length = get_best_neibour(neibours, city_map)
    return current_solution, current_route_length

def main():
    city_map = [[0, 400, 500, 300],
                [400, 0, 300, 500],
                [500, 300, 0, 400],
                [300, 500, 400, 0]]
    print(hillclimbing(city_map))
    
if __name__ == "__main__":
    main()