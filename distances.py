# Weight equivalent to miles
# Mostly from textbook

import csv


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    # def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
    #     self.edge_weights[(from_vertex, to_vertex)] = weight
    #     self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.edge_weights[(vertex_a, vertex_b)] = weight

    # def add_to_adjacency_list(self, packages):
    #     for bucket in packages.table:
    #         for package in bucket:
    #             self.adjacency_list[package[1]].append(package)
    def put_packages_in_delivery_dict(self, ht):
        for bucket in ht.table:
            for item in bucket:
                self.adjacency_list[item[1]].append(item)


def get_distance_data(file):
    data = []
    with open(file) as f:
        reader = csv.reader(open(file))

        next(reader, None)
        for row in reader:
            data.append(row)
    return data


def get_address_data(address_file):
    address_data = []
    with open(address_file) as file:
        reader = csv.reader(open(address_file))

        next(reader, None)
        for row in reader:
            address_data.append(row[1])
    return address_data


def create_graph(file):
    data = get_distance_data(file)
    graph = Graph()

    for row in data:
        # print(row[3])
        graph.add_vertex(row[1])  # vertex = address
    for row in data:
        for i in range(3, len(row)):
            graph.add_undirected_edge(row[1], data[i - 3][1], float(row[i]))  # edge = distances
    return graph


addresses = get_address_data("addressCSV.csv")
# print(addresses)

wgu_graph = create_graph("wgups_distances.csv")
# print(wgu_graph.adjacency_list.keys())
# print(wgu_graph.edge_weights)
# print("Edge Weight: " + str(wgu_graph.edge_weights['300 State St', '6351 South 900 East'])) # How to check distance between two addresses
# print(wgu_graph.edge_weights)
