from distances import wgu_graph


def greedy_algorithm(route):
    distances = wgu_graph.edge_weights
    route_to_optimize = route
    hub = "4001 South 700 East"
    best_route = [hub]

    total_dist = 0
    while len(route_to_optimize) != 0:
        min_dist = [0, hub]
        for address in route_to_optimize:
            dist = distances[best_route[-1], address]
            if min_dist[0] == 0:
                temp = [dist, address]
            if dist < temp[0] and dist != 0:
                temp = [dist, address]
        if temp[1] not in best_route:
            best_route.append(temp[1])
            total_dist += dist
            # print("min: " + str(temp))
        route_to_optimize.remove(temp[1])

    # print("DIST: " + str(total_dist))

    return best_route


def greedy_algorithm_distance(route):
    distances = wgu_graph.edge_weights
    route_to_optimize = route
    hub = "4001 South 700 East"
    best_route = [hub]

    total_dist = 0
    while len(route_to_optimize) != 0:
        min_dist = [0, hub]
        for address in route_to_optimize:
            dist = distances[best_route[-1], address]
            if min_dist[0] == 0:
                temp = [dist, address]
            if dist < temp[0] and dist != 0:
                temp = [dist, address]
        if temp[1] not in best_route:
            best_route.append(temp[1])
            total_dist += dist
            # print("min: " + str(temp))
        route_to_optimize.remove(temp[1])

    # print("DIST: " + str(total_dist))

    return total_dist


def get_total_distance(truck1, truck2, truck3):
    dist1 = greedy_algorithm_distance(truck1.route)
    dist2 = greedy_algorithm_distance(truck2.route)
    dist3 = greedy_algorithm_distance(truck3.route)

    sum = dist1 + dist2 + dist3

    return sum
